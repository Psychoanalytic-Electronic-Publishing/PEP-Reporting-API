import os
os.environ["CORS_ORIGIN"] = "https://stage.pep-web.org"

from main.helpers.response_helper import ResponseHelper
from main.config import Config
import json

def test_ResponseHelper_create_response_works():
    response = ResponseHelper.create_response({"message": "hello"})

    assert response['statusCode'] == 200
    assert response['headers']['Access-Control-Allow-Origin'] == Config.CORS_ORIGIN
    assert response['headers']['Access-Control-Allow-Credentials'] == True
    assert response['headers']['Content-Type'] == 'application/json'
    assert response['body'] == json.dumps({"message": "hello"})

    response = ResponseHelper.create_response({"message": "hello"}, 500)

    assert response['statusCode'] == 500
    