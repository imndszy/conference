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
