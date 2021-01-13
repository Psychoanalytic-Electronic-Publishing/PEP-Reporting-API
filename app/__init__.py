# app/__init__.py

import collections

from flask_restx import Api
from flask_restx.representations import output_json
from flask import Blueprint, json

def create_blueprint(apiname='api'):
    from .main.decorators import before_request, after_request

    blueprint = Blueprint(apiname, __name__)

    #add decorators to blueprint
    blueprint.before_request(before_request)
    blueprint.after_app_request(after_request)

    return blueprint

def create_api(blueprint):
    from .main.controller.data_error_controller import api as data_error_ns
    from .main.controller.feedback_controller import api as feedback_ns

    api = Api(blueprint,
            title='PEP Reporting API',
            version='1.0',
            description='An API for reporting PEP errors'
            )

    api.representations = collections.OrderedDict()
    api.representations["application/vnd.api+json"] = output_json

    api.add_namespace(data_error_ns, path='/data-errors')
    api.add_namespace(feedback_ns, path='/feedback')

    return api
