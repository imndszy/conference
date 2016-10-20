# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DB_HOSTNAME = 'localhost'
DB_PORT = 3306
DB_USERNAME = 'szy'
DB_PASSWORD = '123456'
DB_NAME = 'conference'
APP_ID = ''
SECRET = ''
TOKEN = ''

MENU = {
    "button": [
        {
            "type": "view",
            "name": "会务信息",
            "url": "http://www.njuszy.cn"

        },
        {
            "type": "view",
            "name": "您的行程",
            "url": "http://www.njuszy.cn/arrive"

        },
        {
            "type": "view",
            "name": "其他信息",
            "url": "http://www.njuszy.cn/introduce"
        }

    ]
}
