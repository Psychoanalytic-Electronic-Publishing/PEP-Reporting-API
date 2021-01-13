class Error():
    def __init__(self, code, entity=None, status_code=None, detail=None):
        self.code = code
        self.entity = entity
        self.detail = detail
        self.status_code = status_code

def errorstore(cls):
    cls.create_error_codes()
    return cls

@errorstore
class ErrorStore():
    """ Error store for common error codes """
    
    #default entity and status code
    entity = "system"
    status_code = 400

    #common error code strings
    RequiredAttributeMissing = None
    InvalidInclude = None
    CannotDelete = None

    @classmethod
    def create_error_codes(cls):
        cls.RequiredAttributeMissing = cls.create_error("requiredAttributeMissing")
        cls.InvalidInclude = cls.create_error("invalidInclude")
        cls.CannotDelete = cls.create_error("cannotDelete")

    @classmethod
    def create_error(cls, code, entity=None, status_code=None, detail=None):
        _entity = entity or cls.entity
        _status_code = status_code or cls.status_code
        return Error(code, entity=_entity, status_code=_status_code, detail=detail)
