from marshmallow_jsonapi import fields
from marshmallow.validate import Length
from .base.base_schema import BaseSchema
from .base.base_query_param_schema import BaseQueryParamSchema

class DataErrorSchema(BaseSchema):

    """ DataError Marshmallow Schema """
    id = fields.Integer(dump_only=True)
    username = fields.Str(attribute="username", required=False, validate=Length(max=256), missing="")
    email = fields.Str(attribute="email", required=True, validate=Length(max=256))
    full_name = fields.Str(attribute="full_name", required=True, validate=Length(max=256))

    problem_text = fields.Str(attribute="problem_text", required=False, validate=Length(max=1024), missing="")
    corrected_text = fields.Str(attribute="corrected_text", required=True, validate=Length(max=1024))

    url_problem_page = fields.Str(attribute="url_problem_page", required=True, validate=Length(max=256))
    additional_info = fields.Str(attribute="additional_info", required=False, validate=Length(max=1024), missing="")

    is_author_publisher = fields.Boolean(attribute="is_author_publisher", required=True)
    has_original_copy = fields.Boolean(attribute="has_original_copy", required=True)

    date_created = fields.Str(attribute="date_created", dump_only=True)
    date_modified = fields.Str(attribute="date_modified", dump_only=True)
    is_active = fields.Boolean(attribute="is_active")
