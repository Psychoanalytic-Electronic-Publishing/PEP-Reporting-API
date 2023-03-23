from app.main.config import Config
from github import Github


class GitHubHelper:
    @staticmethod
    def create_issue(subject, description, assignees):
        git_client = Github(Config.GITHUB_TOKEN)
        repo = git_client.get_repo(Config.GITHUB_REPO)
        resp = repo.create_issue(
            title=subject,
            body=description,
            labels=Config.GITHUB_LABELS,
            assignees=assignees
        )
        return resp
