# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.db import insert, create_engine, select
from app.config import DB_USERNAME,DB_PASSWORD,DB_NAME,DB_HOSTNAME,DB_PORT

def handle_arrive_post(**kw):
    print 'asds'
    create_engine(DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOSTNAME, DB_PORT, charset='utf8')
    return insert('wechat',**kw)
