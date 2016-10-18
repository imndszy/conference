# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
from app.db import insert, create_engine, select, update


def handle_arrive_post(**kw):
    result = select('select * from wechat1 where username=? and school=?', kw['username'], kw['school'])
    if result:
        print 'delete',update('delete from wechat1 where username=? and school = ?',kw['username'], kw['school'])
    return insert('wechat1',**kw)

def handle_arrive_post_2(**kw):
    result = select('select * from wechat2 where username=? and school=?', kw['username'], kw['school'])
    if result:
        print 'delete',update('delete from wechat2 where username=? and school = ?',kw['username'], kw['school'])
    return insert('wechat2',**kw)


def handle_arrive_get(username,school):
    return select('select * from wechat1 where username=? and school=?',username,school)

