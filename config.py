import os


# default config
class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = '\xcb\xa2\x92\xa206]\xd0\xdb\xfe\x9e\xa0\xab\x9d\xc4@\xd0\xf1\xa4\x15\xab\x1a)\xca'
    # SECRET_KEY = os.urandom(25)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
