import os


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    # Secret key for the app
    SECRET_KEY = os.environ['SECRET_KEY']
    # Database URI that is written in venv/bin/activate
    try:
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    except KeyError:
        pass
    # Credentials to access typeform API (https://admin.typeform.com/account)
    TYPEFORM_FORM_UID = os.environ['TYPEFORM_FORM_UID']
    TYPEFORM_API_KEY = os.environ['TYPEFORM_API_KEY']
    # Credentials for admin
    ADMIN_USER = os.environ['ADMIN_USER']
    ADMIN_PASS = os.environ['ADMIN_PASS']


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
