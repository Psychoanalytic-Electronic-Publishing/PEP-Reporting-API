from main.service.feedback_service import FeedbackService
from main.schema.feedback_schema import FeedbackSchema
from marshmallow import EXCLUDE


create_schema = FeedbackSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    data = create_schema.loads(event['body'])
    return FeedbackService.create_issue(data=data)
