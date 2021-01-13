from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask import json
from app.main import create_app
from app import create_blueprint, create_api
from generate_routes import RouteGenerator

app = create_app()

blueprint = create_blueprint()
api = create_api(blueprint)

app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)


route_generator = RouteGenerator()

@manager.command
def run():
    app.run()

@manager.command
def generate_routes():
    dump("information.json")
    route_generator.generate_serverless_route_configs("route_configs.yml", "unauthorized-endpoints.txt")

@manager.command
def dump(file):
    f = open(file, "a")
    f.truncate(0)
    f.write(json.dumps(api.__schema__, indent=2))
    f.close()

if __name__ == '__main__':
    manager.run()

