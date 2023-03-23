import os


class Config:
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
    GITHUB_REPO = os.environ.get("GITHUB_REPO")
    GITHUB_LABELS = os.environ.get("GITHUB_LABELS").split(
        ",") if os.environ.get("GITHUB_LABELS") else []
    GITHUB_ASSIGNEES_FEEDBACK = os.environ.get("GITHUB_ASSIGNEES_FEEDBACK").split(
        ",") if os.environ.get("GITHUB_ASSIGNEES_FEEDBACK") else []
    GITHUB_ASSIGNEES_DATAERROR = os.environ.get("GITHUB_ASSIGNEES_DATAERROR").split(
        ",") if os.environ.get("GITHUB_ASSIGNEES_DATAERROR") else []
