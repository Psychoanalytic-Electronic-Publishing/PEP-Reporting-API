from app.main.service.data_error_service import DataErrorService
from app.main.schema.data_error_schema import DataErrorSchema

create_schema = DataErrorSchema(unknown="EXCLUDE")

def handler(event, context):
    print(event)

    data = create_schema.loads(event['body'])
    return DataErrorService.save_new_data_error(data=data)