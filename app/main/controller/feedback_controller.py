from flask import request
from flask_restx import Resource, Namespace
from flask_accepts import accepts, responds
from app.main.config import Config

from app.main.service.feedback_service import FeedbackService
from app.main.schema.feedback_schema import FeedbackSchema
from app.main import app

api = Namespace('feedback', description='feedback related operations')

#schemas
default_schema = FeedbackSchema()
list_schema = FeedbackSchema(many=True)
create_schema = FeedbackSchema(unknown="EXCLUDE")

@api.route('/')
class FeedbackResource(Resource):

    @responds(schema=default_schema, api=api)
    @accepts(schema=create_schema, api=api)
    @api.doc('createFeedback')
    def post(self):
        """Creates a new Feedback """
        data = create_schema.load(request.get_json())
        return FeedbackService.create_issue(data=data)
