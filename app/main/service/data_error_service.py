from app.main.exceptions.flask_exceptions import GenericException, EntityNotFoundException
from .base.base_service import BaseService
from app.main.config import Config
from app.main.helpers.dynamodb_helper import DynamoDbHelper
from app.main.helpers.sns_helper import SnsHelper
from flask import current_app as app
import datetime
import time

class DataErrorService(BaseService):
    @staticmethod
    def save_new_data_error(data):
        # save data error to dynamodb
        data['id'] = int(time.time())
        data['date_created'] = datetime.datetime.utcnow().isoformat()
        data['date_modified'] = data['date_created']
        data['is_active'] = True
        resp = DynamoDbHelper.save_data_error(data)
        data_error_item = DynamoDbHelper.get_data_error(data['id'])

        # send data error email
        try:
            SnsHelper.send_message_to_topic(
                app.config[Config.DATA_ERROR_TOPIC_ARN],
                app.config[Config.DATA_ERROR_EMAIL_SUBJECT],
                get_formatted_data_error_email_body(data_error_item),
                get_formatted_data_error_sms_body(data_error_item))
        except Exception as e:
            app.logger.error(e)

        return {"data": data_error_item, "includes": []}

def get_formatted_data_error_email_body(data_error_item):
    return """Hello,
A PEP data error has been reported by {full_name}.

Username: "{username}"
Email: "{email}"
Author or Publisher?: {is_author_publisher}
Has original paper?: {has_original_copy}
URL: "{url_problem_page}"

Problem Text: "{problem_text}"

Corrected text: "{corrected_text}"

Additional Info: "{additional_info}"

Thanks,
The PEP Team""".format(
    full_name=data_error_item['full_name'],
    username=data_error_item['username'],
    email=data_error_item['email'],
    is_author_publisher=data_error_item['is_author_publisher'],
    has_original_copy=data_error_item['has_original_copy'],
    url_problem_page=data_error_item['url_problem_page'],
    problem_text=data_error_item['problem_text'],
    corrected_text=data_error_item['corrected_text'],
    additional_info=data_error_item['additional_info']
    )

def get_formatted_data_error_sms_body(data_error_item):
    return "A PEP data error has been reported by {full_name}.".format(
        full_name=data_error_item['full_name'])
