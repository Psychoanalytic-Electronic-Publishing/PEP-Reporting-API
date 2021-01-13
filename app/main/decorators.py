""" Decorators for handling before and after requests and any other misc functionality """
from datetime import datetime
from flask import request
from flask import current_app as app
from sqlalchemy.exc import DatabaseError



def conditionally(dec, cond):
    """ conditionally call another decorator """
    def resdec(f):
        if not cond:
            return f
        return dec(f)
    return resdec

def before_request():
    """ run before every request """
    #log all request data
    timestamp = datetime.now().strftime('[%Y-%b-%d %H:%M]')
    app.logger.debug('[REQUEST] %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path)
    app.logger.debug('[REQUEST] Headers: %s', request.headers)
    app.logger.debug('[REQUEST] Body: %s', request.get_data())

def after_request(response):
    """ run after every request """
    #log all response data
    timestamp = datetime.now().strftime('[%Y-%b-%d %H:%M]')
    app.logger.debug('[RESPONSE] %s %s %s %s %s %s', timestamp, request.remote_addr, request.method, request.scheme, request.full_path, response.status)

    try:
        response.headers['Web-Version'] = request.environ.get('event').get('stageVariables').get('webVersion')
    except Exception as e:
        print(e)

    app.logger.debug('[RESPONSE] Headers : %s', response.headers)
    return response
