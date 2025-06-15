import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'SECRET_KEY_NOT_SET')
    PHRASE_API_URL = 'http://free-generator.ru/generator.php'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True

    @classmethod
    def init_app(cls, app):
        print('!!!Run application in development mode..!!!')


class TestingConfig(Config):
    TESTING = True

    @classmethod
    def init_app(cls, app):
        print('!!!Run application in testing mode.!!!')


class ProductionConfig(Config):
    DEBUG = False
    USE_RELOADER = False

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'default': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
