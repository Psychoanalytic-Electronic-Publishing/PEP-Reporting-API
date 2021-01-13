from marshmallow import pre_dump, post_load
from marshmallow_jsonapi import Schema, fields, SchemaOpts
from inflection import pluralize
from case_conversion import camelcase, dashcase, snakecase
import ujson

class BaseSchema(Schema):
    """ Base Marshmallow Schema """

    #temp_id for sideposting
    temp_id = fields.String()
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__.replace('Schema', '').replace('Preview', '')
        meta_name = kwargs.pop("type_name", pluralize(class_name))
        self.opts.__init__(self.Meta(meta_name))
        super().__init__(*args, **kwargs)

    @pre_dump(pass_many=True)
    def process_pre_dump(self, in_data, **kwargs):
        self.check_relations(self.include_data)
        if isinstance(in_data, list):
            if not isinstance(in_data[0], dict):
                return in_data
            in_data = in_data[0]
        if isinstance(in_data, dict):
            self.check_relations(in_data['includes'], temporary=True)
            if 'total_count' in in_data:
                self.set_count_meta(in_data['total_count'])
            elif 'meta' in in_data:
                self.document_meta = in_data['meta']
            self.document_meta = {camelcase(k):v for k, v in self.document_meta.items()}
            return in_data['data']
        return in_data

    def set_count_meta(self, total_count):
        self.document_meta = {"total_count" : total_count}

    @post_load(pass_many=True)
    def snakify_input(self, data, many, **kwargs):
        def from_dict(data):
            return {snakecase(k):v for k, v in data.items()}
        if many:
            return [from_dict(item) for item in data]
        return from_dict(data)

    class Meta():
        datetimeformat = '%Y-%m-%dT%H:%M:%S.%fZ'
        type_ = "default"
        json_module = ujson
        def __init__(self, meta_name):
            self.type_ = camelcase(meta_name)
            self.self_view = dashcase(meta_name) + '-detail'
            self.self_view_kwargs = {'id': '<id>'}
            self.self_view_many = dashcase(meta_name) + '-list'
            self.inflect = camelcase
