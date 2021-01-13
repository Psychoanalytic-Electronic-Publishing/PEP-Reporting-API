import datetime
from pytest import fixture
from flask import request
from typing import List
from unittest.mock import patch
from unittest.mock import Mock
from app.test.fixtures import app
from app.main.service.feedback_service import FeedbackService
from app.main.service.feedback_service import get_formatted_issue_body
from app.main.service.feedback_service import get_formatted_issue_subject
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
                "browser": "firefox"
            }
        }
    }
)


@patch.object(GitHubHelper, 'create_issue')
def test_save_new_data_error(githubhelper_mock, app):  # noqa
    with app.app_context():
        resp = FeedbackService.create_issue(feedback)

        githubhelper_mock.assert_called_once()
        output = resp.get('data')
        assert output['subject'] == feedback['subject']
        assert output['description'] == feedback['description']
        assert output['url'] == feedback['url']
        assert output['feedback_type'] == feedback['feedback_type']
        assert output['browser'] == feedback['browser']


def test_get_formatted_issue_subject():  # noqa
    resp = get_formatted_issue_subject(feedback)
    assert resp == f"[{feedback['feedback_type']}] {feedback['subject']}"


def test_get_formatted_issue_body():  # noqa
    resp = get_formatted_issue_body(feedback)
    assert resp == f"""
URL: {feedback['url']}
Browser: {feedback['browser']}

{feedback['description']}
"""
