from main.service.data_error_service import DataErrorService
from main.schema.data_error_schema import DataErrorSchema
from marshmallow import EXCLUDE
import json
from main.config import Config

create_schema = DataErrorSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    try:
        data = create_schema.loads(event['body'])
        resp = DataErrorService.save_new_data_error(data=data)

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": Config.CORS_ORIGINS,
                "Access-Control-Allow-Credentials": True,
                'Content-Type': 'application/json'
            },
            "body": json.dumps(resp)
        }

    except Exception as e:
        print(e)

        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": Config.CORS_ORIGINS,
                "Access-Control-Allow-Credentials": True,
                'Content-Type': 'application/json'
            },
            "body": json.dumps({"message": str(e)})
        }
