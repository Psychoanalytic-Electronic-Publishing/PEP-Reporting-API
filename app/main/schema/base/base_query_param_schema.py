from marshmallow import fields, Schema, pre_load, pre_dump
from .base_schema import BaseSchema
from .base_schema_meta import BaseSchemaMeta

class BaseQueryParamSchema(BaseSchema, metaclass=BaseSchemaMeta):

    #define params that are present on every schema
    sort = fields.String()
    limit = fields.Integer()
    offset = fields.Integer()

    #marshmallow jsonapi requires id field
    id = fields.Integer()

    def __init__(self, *args, **kwargs):
        parent = kwargs.pop("parent", None)
        if parent:
            self.fields = parent.fields
        super().__init__(*args, **kwargs)

    def unwrap_request(self, data, many, **kwargs):
        data = {"data": data}
        super().unwrap_request(data, many, **kwargs)