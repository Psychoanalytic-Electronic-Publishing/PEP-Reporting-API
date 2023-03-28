import os


class Config:
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    GITHUB_REPO = os.environ.get("GITHUB_REPO")
    GITHUB_LABELS = os.environ.get("GITHUB_LABELS").split(
        ",") if os.environ.get("GITHUB_LABELS") else []
    GITHUB_ASSIGNEES = os.environ.get("GITHUB_ASSIGNEES").split(
        ",") if os.environ.get("GITHUB_ASSIGNEES") else []
