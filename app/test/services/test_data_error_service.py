import datetime
from pytest import fixture
from flask import request
from typing import List
from unittest.mock import patch
from unittest.mock import Mock
from app.test.fixtures import app
from app.main.service.data_error_service import DataErrorService
from app.main.service.data_error_service import get_formatted_data_error_sms_body
from app.main.service.data_error_service import get_formatted_data_error_email_body
from app.main.schema.data_error_schema import DataErrorSchema
from app.main.helpers.dynamodb_helper import DynamoDbHelper
from app.main.helpers.sns_helper import SnsHelper

schema = DataErrorSchema()
data_error = schema.load(
    {
        "data": {
            "type": "dataErrors",
            "attributes": {
                "username": "OvaltineJenkins",
                "email": "ovaltine.jenkins@gmail.com",
                "fullName": "Ovaltine Jenkins",
                "problemText": "bad",
                "correctedText": "good",
                "urlProblemPage": "https://test.com",
                "isAuthorPublisher": "false",
                "hasOriginalCopy": "true"
            }
        }
    }
)


@patch.object(DynamoDbHelper, 'save_data_error')
@patch.object(DynamoDbHelper, 'get_data_error')
@patch.object(SnsHelper, 'send_message_to_topic')
def test_save_new_data_error(save_data_error_mock, get_data_error_mock, send_message_to_topic_mock, app):  # noqa
    with app.app_context():
        get_data_error_mock.return_value = data_error

        DataErrorService.save_new_data_error(data_error)

        save_data_error_mock.assert_called_once()
        get_data_error_mock.assert_called_once()
        send_message_to_topic_mock.assert_called_once()


def test_get_formatted_data_error_sms_body():  # noqa
    resp = get_formatted_data_error_sms_body(data_error)
    assert resp == "A PEP data error has been reported by Ovaltine Jenkins."


def test_get_formatted_data_error_email_body():  # noqa
    resp = get_formatted_data_error_email_body(data_error)
    assert resp == f"""Hello,
A PEP data error has been reported by {data_error['full_name']}.

Username: "{data_error['username']}"
Email: "{data_error['email']}"
Author or Publisher?: {data_error['is_author_publisher']}
Has original paper?: {data_error['has_original_copy']}
URL: "{data_error['url_problem_page']}"

Problem Text: "{data_error['problem_text']}"

Corrected text: "{data_error['corrected_text']}"

Additional Info: "{data_error['additional_info']}"

Thanks,
The PEP Team"""
