from flask import request
from flask_restx import Resource, Namespace
from flask_accepts import accepts, responds
from app.main.config import Config

from app.main.service.data_error_service import DataErrorService
from app.main.schema.data_error_schema import DataErrorSchema
from app.main import app

api = Namespace('data-errors', description='data error related operations')

#schemas
default_schema = DataErrorSchema()
list_schema = DataErrorSchema(many=True)
create_schema = DataErrorSchema(unknown="EXCLUDE")

@api.route('/')
class DataErrorResource(Resource):

    @responds(schema=default_schema, api=api)
    @accepts(schema=create_schema, api=api)
    @api.doc('createDataError')
    def post(self):
        """Creates a new DataError """
        data = create_schema.load(request.get_json())
        return DataErrorService.save_new_data_error(data=data)
