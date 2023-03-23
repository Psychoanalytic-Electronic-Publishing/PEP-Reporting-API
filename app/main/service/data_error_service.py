from .base.base_service import BaseService
from app.main.config import Config
from app.main.helpers.github_helper import GitHubHelper
from app.main.config import Config


class DataErrorService(BaseService):
    @staticmethod
    def save_new_data_error(data):
        resp = GitHubHelper.create_issue(
            get_formatted_issue_subject(data),
            get_formatted_issue_body(data),
            Config.GITHUB_ASSIGNEES_DATAERROR
        )
        data['id'] = resp.number
        return {"data": data, "includes": []}


def get_formatted_issue_subject(data):
    return "[{issue_type}] {subject}".format(
        issue_type='DATA',
        subject=data['url_problem_page']
    )


def get_formatted_issue_body(data_error_item):
    return """A PEP data error has been reported by {full_name}.

Username: "{username}"
Email: "{email}"
Author or Publisher?: {is_author_publisher}
Has original paper?: {has_original_copy}
URL: "{url_problem_page}"

Problem Text: "{problem_text}"

Corrected text: "{corrected_text}"

Additional Info: "{additional_info}"
""".format(
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
