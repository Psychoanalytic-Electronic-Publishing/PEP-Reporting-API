import datetime
from pytest import fixture
from typing import List
from unittest.mock import patch
from unittest.mock import Mock
from app.test.fixtures import app
from app.main.service.data_error_service import DataErrorService
from app.main.service.data_error_service import get_formatted_issue_body, get_formatted_issue_subject
from app.main.schema.data_error_schema import DataErrorSchema
from app.main.helpers.github_helper import GitHubHelper

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


@patch.object(GitHubHelper, 'create_issue')
def test_save_new_data_error(githubhelper_mock, app):  # noqa
    with app.app_context():
        resp = DataErrorService.save_new_data_error(data_error)

        githubhelper_mock.assert_called_once()
        output = resp.get('data')
        assert output['username'] == data_error['username']


def test_get_formatted_issue_subject():  # noqa
    resp = get_formatted_issue_subject(data_error)
    assert resp == "[DATA] https://test.com"


def test_get_formatted_issue_body():  # noqa
    resp = get_formatted_issue_body(data_error)
    assert resp == f"""A PEP data error has been reported by Ovaltine Jenkins.

Username: "OvaltineJenkins"
Email: "ovaltine.jenkins@gmail.com"
Author or Publisher?: False
Has original paper?: True
URL: "https://test.com"

Problem Text: "bad"

Corrected text: "good"

Additional Info: ""
"""
