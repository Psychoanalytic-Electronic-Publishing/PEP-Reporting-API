from flask import current_app as app
from app.main.config import Config
from github import Github

class GitHubHelper:
    @staticmethod
    def create_issue(subject, description, assignees):
        git_client = Github(app.config[Config.GITHUB_TOKEN])
        repo = git_client.get_repo(app.config[Config.GITHUB_REPO])
        resp = repo.create_issue(
            title=subject,
            body=description,
            labels=app.config[Config.GITHUB_LABELS],
            assignees=assignees
        )
        return resp
