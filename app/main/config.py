import os
import json
from distutils import util
import base64
import boto3
basedir = os.path.abspath(os.path.dirname(__file__))
kms = boto3.client('kms')


class Config:

    AWS_REGION = "AWS_REGION"
    AWS_PROFILE = "AWS_PROFILE"
    DEBUG = "DEBUG"
    USE_ENCRYPTION = "USE_ENCRYPTION"
    PROPAGATE_EXCEPTIONS = "PROPAGATE_EXCEPTIONS"
    DATA_ERROR_TOPIC_ARN = "DATA_ERROR_TOPIC_ARN"
    DATA_ERROR_EMAIL_SUBJECT = "DATA_ERROR_EMAIL_SUBJECT"
    PRESERVE_CONTEXT_ON_EXCEPTION = "PRESERVE_CONTEXT_ON_EXCEPTION"
    DYNAMODB_TABLE_DATA_ERROR = "DYNAMODB_TABLE_DATA_ERROR"
    GITHUB_TOKEN = "GITHUB_TOKEN"
    GITHUB_REPO = "GITHUB_REPO"
    GITHUB_LABELS = "GITHUB_LABELS"
    GITHUB_ASSIGNEES = "GITHUB_ASSIGNEES"

    def __init__(self, environment: str = None):
        self.config_values = ConfigValues(environment)


class ConfigValues:
    def __init__(self, environment: str = None):

        self.requested_environment: str = os.getenv('CONFIG_ENV', "local")
        self.force_environment: bool = False
        if environment is not None:
            self.requested_environment = environment
            self.force_environment = True

        with open("flask-config-overwrite.json", 'r') as f:
            overwrite = json.load(f)
            if "environments" in overwrite:
                if "active" in overwrite and overwrite["active"] in overwrite["environments"]:
                    self.__overwrite_config_dict = overwrite["environments"].get(
                        overwrite["active"])
                else:
                    # grab first entry if active not set
                    self.__overwrite_config_dict = next(
                        iter(overwrite["environments"].values()))
            else:
                self.__overwrite_config_dict = overwrite

        with open("flask-config.json", 'r') as f:
            self.__default_config_dict = json.load(f)["default"]

        with open("flask-config.json", 'r') as f:
            self.__environment_config_dict = json.load(
                f)[self.requested_environment]

        # init values
        self.USE_ENCRYPTION = self.__get_config_value(
            Config.USE_ENCRYPTION, self.__string_to_bool) or False
        self.DEBUG = self.__get_config_value(
            Config.DEBUG, self.__string_to_bool) or False
        self.PRESERVE_CONTEXT_ON_EXCEPTION = self.__get_config_value(
            Config.PRESERVE_CONTEXT_ON_EXCEPTION, self.__string_to_bool) or False
        self.PROPAGATE_EXCEPTIONS = self.__get_config_value(
            Config.PROPAGATE_EXCEPTIONS, self.__string_to_bool) or False
        self.DATA_ERROR_TOPIC_ARN = self.__get_config_value(
            Config.DATA_ERROR_TOPIC_ARN) or ""
        self.DATA_ERROR_EMAIL_SUBJECT = self.__get_config_value(
            Config.DATA_ERROR_EMAIL_SUBJECT) or ""
        self.DYNAMODB_TABLE_DATA_ERROR = self.__get_config_value(
            Config.DYNAMODB_TABLE_DATA_ERROR) or ""
        self.GITHUB_TOKEN = self.__get_config_value(Config.GITHUB_TOKEN) or ""
        self.GITHUB_REPO = self.__get_config_value(Config.GITHUB_REPO) or ""
        self.GITHUB_LABELS = self.__get_config_value(
            Config.GITHUB_LABELS, self.__string_to_list) or []
        self.GITHUB_ASSIGNEES = self.__get_config_value(
            Config.GITHUB_ASSIGNEES, self.__string_to_list) or []

        # setup default client w/ provided or default region and profile
        self.AWS_PROFILE = self.__get_config_value(Config.AWS_PROFILE)
        self.AWS_REGION = self.__get_config_value(Config.AWS_REGION)
        boto3.setup_default_session(
            profile_name=self.AWS_PROFILE, region_name=self.AWS_REGION)

    def __get_config_value(self, key: str, typeConverterMethod=None, isEncrypted=False):
        # retrieve information from environment variable if available
        value = os.getenv(key)

        # if environment variable isn't set, grab from flask-config-overwrite.json file
        if value is None and not self.force_environment:
            value = self.__overwrite_config_dict.get(key)

        # if still not set, look into the environment specific configs
        if value is None:
            value = self.__environment_config_dict.get(key)

        # if all above failed, resolve to default
        if value is None:
            value = self.__default_config_dict.get(key)

        if value is not None and typeConverterMethod is not None:
            value = typeConverterMethod(value)

        # decrypt from base64 if needed
        if value is not None and isEncrypted is True and self.USE_ENCRYPTION is True:
            value = kms.decrypt(CiphertextBlob=bytes(base64.b64decode(value)))[
                'Plaintext'].decode()

        return value

    def __string_to_bool(self, value: str) -> bool:
        return bool(util.strtobool(value))

    def __string_to_list(self, value: str) -> list:
        values = [v.strip() for v in value.split(',')]
        return values if '' not in values[:1] else []
