# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask, request, make_response, render_template

from app.config import TOKEN

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET'])
def wechat_auth():
    echostr = request.args.get('echostr', '')
    if verification():
        return make_response(echostr)
    return 'render_template("index.html")'


@app.route('/', methods=['POST'])
def wechat_msg():
    rec = request.data
    msg = parse(rec)
    # if msg['MsgType'] == 'event':
    #     from msg_handler import handle_event
    #     content = handle_event(msg)
    #     return res_text_msg(msg, content)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/arrive')
def arrive():
    return render_template('Arrive.html')

@app.route('/leave')
def depart():
    return render_template('Leave.html')



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

text_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"


def res_text_msg(msg, content):
    response = make_response(text_rep % (msg['FromUserName'], msg['ToUserName'], str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response


if __name__ == "__main__":
    app.run()