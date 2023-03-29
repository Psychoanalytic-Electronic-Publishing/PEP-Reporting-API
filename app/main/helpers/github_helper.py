from main.config import Config
from github import Github, GithubIntegration
import base64


class GitHubHelper:
    @staticmethod
    def create_issue(subject, description, assignees):

        private_key = base64.b64decode(
            Config.GITHUB_PRIVATE_KEY).decode("utf-8")

        integration = GithubIntegration(
            Config.GITHUB_APP_ID, private_key, base_url="https://github.com/api/v3")

        install = integration.get_installation(
            Config.GITHUB_OWNER, Config.GITHUB_REPO)
        access = integration.get_access_token(install.id)

        git_client = Github(login_or_token=access.token,
                            base_url="https://github.com/api/v3")

        repo = git_client.get_repo(
            f"{Config.GITHUB_OWNER}/{Config.GITHUB_REPO}")
        resp = repo.create_issue(
            title=subject,
            body=description,
            labels=Config.GITHUB_LABELS,
            assignees=assignees
        )
        return resp
