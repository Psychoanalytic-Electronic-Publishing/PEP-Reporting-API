from marshmallow.schema import SchemaMeta
from marshmallow import fields
from marshmallow_jsonapi.fields import BaseRelationship

class BaseSchemaMeta(SchemaMeta):

    ordered = True

    @classmethod
    #override to set default fields for query parameters
    def get_declared_fields(mcs, klass, cls_fields, inherited_fields, dict_cls):
        base_fields = ['offset', 'limit', 'sort']
        ignored_fields = ['temp_id']
        declared_fields = super().get_declared_fields(klass, cls_fields, inherited_fields, dict_cls)
        new_fields = {}
        declared_fields = {k:v for k,v in declared_fields.items() if k not in ignored_fields}
        for name, field in declared_fields.items():      
            if isinstance(field, BaseRelationship):
                continue
            field.required = False
            field.load_only = False
            field.dump_only = False
            if name not in base_fields and isinstance(field, (fields.Float, fields.DateTime)):
                #add range fields
                lower_name = '{}_lower'.format(name)
                upper_name = '{}_upper'.format(name)
                new_fields[lower_name] = field.__class__()
                new_fields[upper_name] = field.__class__()
            if name not in ignored_fields:
                new_fields[name] = field
        return new_fields
