# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB_HOSTNAME = 'localhost'
DB_PORT = '3306'
DB_USERNAME = 'root'
DB_PASSWORD = 'hafjd867'
DB_NAME = 'weixin'
APP_ID = ''
SECRET = ''
TOKEN = ''


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'xxxxx'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

MENU = {
    "button": [
        {
            "type": "view",
            "name": "会议相关",
            "url": "http://121.42.216.141"

        },
        {
            "type": "view",
            "name": "赴会方式登记",
            "url": "http://121.42.216.141"

        },
        {
            "type": "view",
            "name": "返程方式登记",
            "url": "http://121.42.216.141"
        }

    ]
}
