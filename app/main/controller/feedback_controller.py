from app.main.service.feedback_service import FeedbackService
from app.main.schema.feedback_schema import FeedbackSchema

create_schema = FeedbackSchema(unknown="EXCLUDE")


def handler(event, context):
    print(event)

    data = create_schema.loads(event['body'])
    return FeedbackService.create_issue(data=data)
