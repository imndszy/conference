# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB_HOSTNAME = 'localhost'
DB_PORT = '3306'
DB_USERNAME = 'szy'
DB_PASSWORD = '123456'
DB_NAME = 'weixin'
APP_ID = 'wx92a9c02f38'
SECRET = 'aed361bef8658588'
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

            "name": "会议相关",
            "sub_button": [
                {
                    "type": "click",
                    "name": "未读消息",
                    "key": "not_read_mes"
                },
                {
                    "type": "view",
                    "name": "历史消息",
                    "url": "https://open.weixin.qq.com/connect/oauth2/authorize?appid=%s"
                           "&redirect_uri=%s"
                           "/history&response_type=code&scope=snsapi_base&state=123&connect_redirect=1#wechat_redirect"
                           % (APP_ID,ADDRESS)
                }#,
                # {
                #     "type": "click",
                #     "name": "近期消息",
                #     "key": "recent_mes"
                # }
                ]

        },
        {
            "name": "赴会方式登记",
            "sub_button": [
                {
                    "type": "click",
                    "name": "日常考核",
                    "key": "daily_assess"
                },
                {
                    "type": "click",
                    "name": "绩点查询",
                    "key": "gpa"
                },
                {
                    "type": "click",
                    "name": "推免查询",
                    "key": "recom"
                },
                {
                    "type": "click",
                    "name": "导师查询",
                    "key": "tutor"
                }
            ]
        },
        {
            "name": "返程方式",
            "sub_button": [
                {
                    "type": "view",
                    "name": "微信问问",
                    "url": "http://121.42.216.141"
                },
                {
                    "type": "view",
                    "name": "教务推送",
                    "url": "http://121.42.216.141"
                },
                {
                    "type": "scancode_push",
                    "name": "扫码推事件",
                    "key": "rselfmenu_0_1",
                    "sub_button": []
                }
            ]

        }

    ]
}
