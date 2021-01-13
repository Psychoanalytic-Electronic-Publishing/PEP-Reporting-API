from flask import jsonify
from app.main.error_store import Error

class NoneError():
    def __init__(self):
        self.code = None
        self.entity = None
        self.detail = None
        self.status_code = None

class GenericException(Exception):
    status_code = 400

    def __init__(self, **kwargs):
        Exception.__init__(self)
        error = kwargs.pop('error', NoneError())
        self.code = kwargs.pop('code', None) or error.code
        self.entity = kwargs.pop('entity', None) or error.entity
        self.detail = kwargs.pop('detail', None) or error.detail
        self.status_code = kwargs.pop('status_code', None) or error.status_code or GenericException.status_code
        self.meta = kwargs.pop('meta', None)
        self.payload = kwargs.pop('payload', None)

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['errors'] = []
        error = {}
        error['code'] = self.code
        error['meta'] = self.meta or {}
        if self.entity:
            error['meta']['entity'] = self.entity
        if self.detail:
            error['detail'] = self.detail
        rv['errors'].append(error)
        return rv

class EntityNotFoundException(GenericException):
    def __init__(self, entity="system"):
        Exception.__init__(self)
        self.code = "notFound"
        self.entity = entity
        self.status_code = 404

    def to_dict(self):
        rv = dict()
        rv['errors'] = []
        error = {}
        error['code'] = self.code
        error['meta'] = {}
        error['meta']['entity'] = self.entity
        rv['errors'].append(error)
        return rv

