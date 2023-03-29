import os


class Config:
    CORS_ORIGIN = os.environ.get("CORS_ORIGIN")
    GITHUB_PRIVATE_KEY = os.environ.get("GITHUB_PRIVATE_KEY")
    GITHUB_APP_ID = os.environ.get("GITHUB_APP_ID")
    GITHUB_OWNER = os.environ.get("GITHUB_OWNER")
    GITHUB_REPO = os.environ.get("GITHUB_REPO")
    GITHUB_LABELS = os.environ.get("GITHUB_LABELS").split(
        ",") if os.environ.get("GITHUB_LABELS") else []
    GITHUB_ASSIGNEES = os.environ.get("GITHUB_ASSIGNEES").split(
        ",") if os.environ.get("GITHUB_ASSIGNEES") else []
