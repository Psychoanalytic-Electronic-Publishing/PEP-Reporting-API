from app.main.exceptions.flask_exceptions import GenericException, EntityNotFoundException
from .base.base_service import BaseService
from app.main.helpers.github_helper import GitHubHelper
from flask import current_app as app

class FeedbackService(BaseService):
    @staticmethod
    def create_issue(data):
        resp = GitHubHelper.create_issue(
            get_formatted_issue_subject(data),
            get_formatted_issue_body(data)
        )
        data['id'] = resp.number
        return {"data": data, "includes": []}


def get_formatted_issue_subject(feedback):
    return "[{issue_type}] {subject}".format(
        issue_type=feedback['feedback_type'],
        subject=feedback['subject']
    )


def get_formatted_issue_body(feedback):
    return """
URL: {url}
Browser: {browser}
Reporter: {reporter_name}

{description}
""".format(
        url=feedback['url'],
        browser=feedback['browser'],
        reporter_name=feedback['reporter_name'],
        description=feedback['description']
    )
