from decouple import config


class Config(object):
    SECRET_KEY = config('SECRET_KEY', default='guess-me')
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True



