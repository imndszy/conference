# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.db import insert, select, update


def handle_arrive_post(**kw):
    result = select('select * from wechat where username=? and school=?', kw['username'], kw['school'])
    if result:
        update('delete from wechat where username=? and school = ?',kw['username'], kw['school'])
    return insert('wechat',**kw)
