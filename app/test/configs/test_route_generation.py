from pytest import fixture
from app.test.fixtures import app # noqa
from generate_routes import RouteGenerator

@fixture
def route_generator() -> RouteGenerator: return RouteGenerator()

def test_wildcard_unauthorized(route_generator: RouteGenerator):
    yaml_dict = route_generator.build_dictionary("app/test/configs/unauthorized_wildcard.txt")

    for endpoint in yaml_dict:
        if endpoint == "app": continue
        for event in yaml_dict[endpoint]["events"]:
            if type(event) is dict and "http" in event:
                assert "authorizer" not in event["http"]

def test_all_authorized(route_generator: RouteGenerator):
    yaml_dict = route_generator.build_dictionary("app/test/configs/all_authorized.txt")
    for endpoint in yaml_dict:
        if endpoint == "app": continue
        for event in yaml_dict[endpoint]["events"]:
            if type(event) is dict and "http" in event:
                assert "authorizer" in event["http"]

def test_some_unauthorized(route_generator: RouteGenerator):
    unauthorized_routes = ["getAllUsers", "createUser"]
    yaml_dict = route_generator.build_dictionary("app/test/configs/some_unauthorized.txt")
    for endpoint in yaml_dict:
        if endpoint == "app": continue
        for event in yaml_dict[endpoint]["events"]:
            if type(event) is dict and "http" in event:
                if endpoint in unauthorized_routes:
                    assert "authorizer" not in event["http"]
                else:
                    assert "authorizer" in event["http"]
