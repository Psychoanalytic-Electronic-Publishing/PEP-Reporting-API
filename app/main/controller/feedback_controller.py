from main.service.feedback_service import FeedbackService
from main.schema.feedback_schema import FeedbackSchema
from marshmallow import EXCLUDE
import json
from main.config import Config

create_schema = FeedbackSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    try:
        data = create_schema.loads(event['body'])
        return FeedbackService.create_issue(data=data)

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
