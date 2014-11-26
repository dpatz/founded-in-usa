import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # Secret key for the app
    SECRET_KEY = '0123456789'
    # Database URI that is written in venv/bin/activate
    try:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    except KeyError:
        pass
    # Credentials to access typeform API (https://admin.typeform.com/account)
    TYPEFORM_FORM_UID = 'XXXXXX'
    TYPEFORM_API_KEY = '012345...'
    # Credentials for admin
    ADMIN_USER = 'admin'
    ADMIN_PASS = 'password'


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = \
        'postgres://foundedinusa:foundedinusa@localhost:5432/foundedinusa'


class TestingConfig(Config):
    TESTING = True
