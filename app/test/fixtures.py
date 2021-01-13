import pytest
import uuid

from app.main import create_app
from app import create_blueprint, create_api

@pytest.fixture
def app():
    app = create_app("unittests")
    blueprint = create_blueprint(str(uuid.uuid1()))
    api = create_api(blueprint)
    app.register_blueprint(blueprint)
    return app


@pytest.fixture()
def client(app):
    return app.test_client()
