from main.config import Config
import json


class ResponseHelper:
    @staticmethod
    def create_response(data, status=200):
        return {
            "statusCode": status,
            "headers": {
                "Access-Control-Allow-Origin": Config.CORS_ORIGIN,
                "Access-Control-Allow-Credentials": True,
                'Content-Type': 'application/json'
            },
            "body": json.dumps(data)
        }
