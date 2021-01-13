from flask import Flask, jsonify
from flask_cors import CORS
import logging
import boto3
from .config import Config
from app.main.exceptions import GenericException

app = Flask(__name__)

def create_app(environment: str = None):

    logging.basicConfig()

    app.url_map.strict_slashes = False
    config = Config(environment)
    app.config.from_object(config.config_values)
    CORS(app, origins='*', supports_credentials=True, expose_headers='Authorization', allow_headers='*')

    return app


@app.errorhandler(GenericException)
def handle_generic_exception(error):
    """ Handles custom exceptions """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    app.logger.error('[ERROR] Handled exception: {}'.format(error))
    return response

#unhandled exception
@app.errorhandler(Exception)
def all_exception_handler(exception):
    response = {"errors" :
        [{
            "code": "unhandledException",
            "detail":str(exception),
            "meta":{"entity":"system"}
        }]
    }
    app.logger.error('[ERROR] Unhandled exception: {}'.format(str(exception)), exc_info=True)
    return jsonify(response), 500, {'Content-Type': 'application/json'}
