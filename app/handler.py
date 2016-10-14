# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.db import insert, select


def handle_arrive_post(**kw):
    return insert('wechat',**kw)
