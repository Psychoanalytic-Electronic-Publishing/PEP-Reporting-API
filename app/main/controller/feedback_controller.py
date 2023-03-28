from main.service.feedback_service import FeedbackService
from main.schema.feedback_schema import FeedbackSchema
from marshmallow import EXCLUDE
import json

create_schema = FeedbackSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    try:
        data = create_schema.loads(event['body'])
        return FeedbackService.create_issue(data=data)

        return {
            "statusCode": 200,
            "body": resp
        }

    except Exception as e:
        print(e)

        return {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }
