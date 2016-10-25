# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask, request, make_response, render_template, session, jsonify

from app.config import TOKEN
from app.handler import handle_arrive_post
from app.db import create_engine
from app.config import DB_HOSTNAME,DB_PORT,DB_NAME,DB_USERNAME,DB_PASSWORD

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'xxxxxxxxxxxxxxxxxxx'


create_engine(DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOSTNAME, DB_PORT, charset='utf8')

@app.route('/', methods=['GET'])
def wechat_auth():
    echostr = request.args.get('echostr', '')
    if verification():
        return make_response(echostr)
    return render_template("index.html")


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def wechat_msg():
    rec = request.data
    msg = parse(rec)
    if msg['MsgType'] == 'event' and msg.get('Event') == 'subscribe':
        return res_text_msg(msg,'感谢关注会议助手！您可以通过下方菜单栏中的“会务信息”以及“其他信息”来了解本次会议，同时您也可以通过点击'
                                '“您的行程”向会务组登记您的相关信息！')
    return ''



@app.route('/introduce')
def introduce():
    return render_template('introduce.html')


@app.route('/arrive')
def arrive():
    session['arrived'] = 'arrived'
    return render_template('Arrive.html')
#
#
# @app.route('/leave')
# def leave():
#     session['left'] = 'left'
#     return render_template('Leave.html')


@app.route('/arrive_post',methods=['POST'])
def arrive_post():
    if session.get('arrived','') == 'arrived':
        da = request.values
        # session.clear()
        session['school'] = da.get('school').encode('utf8')
        session['company'] = da.get('company').encode('utf8')
        session['username'] = da.get('username').encode('utf8')
        session['work'] = da.get('work').encode('utf8')
        session['tel'] = da.get('tel').encode('utf8')
        session['email'] = da.get('email').encode('utf8')
        session['arrive'] = da.get('arrive').encode('utf8')
        session['arrive_time'] = da.get('arrivetime').encode('utf8')
        session['order_num1'] = da.get('ordernum1').encode('utf8')
        session['leave'] = da.get('leave').encode('utf8')
        session['leavetime'] = da.get('leavetime').encode('utf8')
        session['ordernum2'] = da.get('ordernum2').encode('utf8')
        session['visit'] = da.get('visit').encode('utf8')
        session['finished'] = 'finished'
        session.permanent = True

        handle_arrive_post(school=session['school'],company=session['company'],
                    username=session['username'],work=session['work'],
                    tel=session['tel'],email=session['email'],arrive=session['arrive'],
                    arrivetime=session['arrive_time'],ordernum1=session['order_num1'],
                    visit=session['visit'],leave=session['leave'],
                           leavetime=session['leavetime'],ordernum2=session['ordernum2'])
        return jsonify(result='ok')
    return 'ok'


@app.route('/arrive_get',methods=['GET'])
def arrive_get():
    if request.args.get('num2') == '2' and session.get('finished','') == 'finished':
        # session.clear()
        # result = handle_arrive_get(session.get('username'),session.get('school'))[0]
        return jsonify(result='ok',
                       username=session['username'],
                       school=session['school'],
                       company=session['company'],
                       work=session['work'],
                       tel=session['tel'],
                       email=session['email'],
                       arrivetime=session['arrive_time'],
                       visit=int(session['visit']),
                       ordernum1=session['order_num1'],
                       arrive=int(session['arrive']),
                       leavetime = session['leavetime'],
                       ordernum2 = session['ordernum2'],
                       leave = int(session['leave']))
    return 'ok'

#
# @app.route('/leave_post',methods=['POST'])
# def leave_post():
#     if session.get('left') == 'left':
#         da = request.values
#         session['school'] = da.get('school').encode('utf8')
#         session['username'] = da.get('username').encode('utf8')
#         session['leave'] = da.get('leave').encode('utf8')
#         session['leavetime'] = da.get('leave').encode('utf8')
#         session['ordernum2'] = da.get('ordernum2').encode('utf8')
#         session['finished2'] = 'finished'
#         session.permanent = True
#         handle_arrive_post_2(school=session['school'], username=session['username'],
#                                  leave=int(session['leave']), leavetime=session['leavetime'],
#                                  ordernum2=session['ordernum2'])
#         return jsonify(result='ok')
#     return 'ok'
#
#
# @app.route('/leave_get')
# def leave_get():
#     if request.args.get('num2') == '2' and session.get('finished2') == 'finished':
#         return jsonify(result='ok',
#                        username=session['username'],
#                        school=session['school'],
#                        leavetime=session['leavetime'],
#                        ordernum2=session['ordernum2'],
#                        leave=int(session['leave']))
#     return 'ok'


def parse(rec):
    """
    :param rec: rec is a xml file
    :return: return a dictionary
    """
    root = ET.fromstring(rec)
    msg = {}
    for child in root:
        msg[child.tag] = child.text
    return msg

def verification():
    """
    verify the weixin token
    """
    token = TOKEN
    data = request.args
    signature = data.get('signature', '')
    timestamp = data.get('timestamp', '')
    nonce = data.get('nonce', '')
    s = [timestamp, nonce, token]
    s.sort()
    s = ''.join(s)
    if hashlib.sha1(s).hexdigest() == signature:
        return 1
    return 0


text_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"

news_rep_front = "<xml>\
                <ToUserName><![CDATA[%s]]></ToUserName>\
                <FromUserName><![CDATA[%s]]></FromUserName>\
                <CreateTime>%s</CreateTime>\
                <MsgType><![CDATA[news]]></MsgType>\
                <ArticleCount>%d</ArticleCount>\
                <Articles>"

news_rep_middle = "<item>\
                <Title><![CDATA[%s]]></Title>\
                <Description><![CDATA[%s]]></Description>\
                <PicUrl><![CDATA[%s]]></PicUrl>\
                <Url><![CDATA[%s]]></Url>\
                </item>"

news_rep_back = "</xml>"

def res_text_msg(msg, content):
    response = make_response(text_rep % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response


if __name__ == "__main__":
    app.run()