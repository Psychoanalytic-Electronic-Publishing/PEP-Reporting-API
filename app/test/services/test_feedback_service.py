import datetime
from pytest import fixture
from typing import List
from unittest.mock import patch
from unittest.mock import Mock
from app.main.service.feedback_service import FeedbackService
from app.main.service.feedback_service import get_formatted_issue_body, get_formatted_issue_subject
from app.main.schema.feedback_schema import FeedbackSchema
from app.main.helpers.github_helper import GitHubHelper


schema = FeedbackSchema()
feedback = schema.load(
    {
        "data": {
            "type": "feedbacks",
            "attributes": {
                "subject": "I found a sandwich in one of your parks",
                "description": "i found a sandwich in one of your parks, and i want to know why it didn't have mayonnaise!",
                "url": "https://test.com",
                "feedbackType": "ISSUE",
                "browser": "firefox",
                "reporterName": "ghee buttersnaps",
                "reporterEmail": "ghee@test.com",
            }
        }
    }
)


@patch.object(GitHubHelper, 'create_issue')
def test_save_new_data_error(githubhelper_mock):  # noqa
    resp = FeedbackService.create_issue(feedback)

    githubhelper_mock.assert_called_once()
    output = resp.get('data')
    assert output['subject'] == feedback['subject']
    assert output['description'] == feedback['description']
    assert output['url'] == feedback['url']
    assert output['feedback_type'] == feedback['feedback_type']
    assert output['browser'] == feedback['browser']
    assert output['reporter_name'] == feedback['reporter_name']
    assert output['reporter_email'] == feedback['reporter_email']


def test_get_formatted_issue_subject():  # noqa
    resp = get_formatted_issue_subject(feedback)
    assert resp == "[ISSUE] I found a sandwich in one of your parks"


def test_get_formatted_issue_body():  # noqa
    resp = get_formatted_issue_body(feedback)
    assert resp == f"""
URL: https://test.com
Browser: firefox
Reporter Name: ghee buttersnaps
Reporter Email: ghee@test.com

i found a sandwich in one of your parks, and i want to know why it didn't have mayonnaise!
"""
