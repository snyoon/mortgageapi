import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fake-ke'
    SESSION_TYPE ='redis'
    SESSION_PERMANENT = False
