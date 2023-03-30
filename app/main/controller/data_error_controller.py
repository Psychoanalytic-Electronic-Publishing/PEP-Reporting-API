from main.service.data_error_service import DataErrorService
from main.schema.data_error_schema import DataErrorSchema
from marshmallow import EXCLUDE
import json
from main.config import Config
from main.helpers.response_helper import ResponseHelper
import traceback

create_schema = DataErrorSchema(unknown=EXCLUDE)


def handler(event, context):
    print(event)

    try:
        data = create_schema.loads(event['body'])
        resp = DataErrorService.save_new_data_error(data=data)

        return ResponseHelper.create_response(resp)

    except Exception as e:
        traceback.print_exception(type(e), e, e.__traceback__)

        return ResponseHelper.create_response({"message": str(e)}, 500)
