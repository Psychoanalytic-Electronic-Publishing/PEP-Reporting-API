from main.service.feedback_service import FeedbackService
from main.schema.feedback_schema import FeedbackSchema
from marshmallow import EXCLUDE
import json
from main.config import Config
from main.helpers.response_helper import ResponseHelper
import traceback


create_schema = FeedbackSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    try:
        data = create_schema.loads(event['body'])
        resp = FeedbackService.create_issue(data=data)

        return ResponseHelper.create_response(resp)

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)

        return ResponseHelper.create_response({"message": str(e)}, 500)
