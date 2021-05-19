from marshmallow_jsonapi import fields
from marshmallow.validate import Length, OneOf
from .base.base_schema import BaseSchema
from .base.base_query_param_schema import BaseQueryParamSchema

class FeedbackSchema(BaseSchema):

    """ Feedback Marshmallow Schema """
    id = fields.Integer(dump_only=True)
    subject = fields.Str(attribute="subject", required=True, validate=Length(max=128))
    description = fields.Str(attribute="description", required=True, validate=Length(max=1024))
    url = fields.Str(attribute="url", required=True, validate=Length(max=256))
    feedback_type = fields.Str(attribute="feedback_type", required=True, validate=OneOf(["FEEDBACK", "ISSUE"]))
    browser = fields.Str(attribute="browser", required=True, validate=Length(max=128))
    reporter_name = fields.Str(attribute="reporter_name", required=True, validate=Length(max=128))
    reporter_email = fields.Str(attribute="reporter_email", required=True, validate=Length(max=128))

