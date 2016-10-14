# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import hashlib
import xml.etree.ElementTree as ET
from flask import Flask, request, make_response, render_template, session

from app.config import TOKEN,DB_HOSTNAME,DB_USERNAME,DB_NAME,DB_PASSWORD,DB_PORT
from app.db import create_engine
from app.handler import handle_arrive_post

app = Flask(__name__)
app.debug = True

create_engine(DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOSTNAME, DB_PORT, charset='utf8')


@app.route('/', methods=['GET'])
def wechat_auth():
    echostr = request.args.get('echostr', '')
    if verification():
        return make_response(echostr)
    return 'render_template("index.html")'


@app.route('/', methods=['POST'])
def wechat_msg():
    rec = request.data
    if rec:
        msg = parse(rec)


@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/arrive')
def arrive():
    return render_template('Arrive.html')


@app.route('/leave')
def leave():
    return render_template('Leave.html')


@app.route('/arrive_handler')
def arrive_handler():
    if request.data.get('num') == 1:
        da = request.data
        # session['school'] = da.get('school')
        session['company'] = da.get('company')
        session['username'] = da.get('username')
        # session['work'] = da.get('work')
        # session['tel'] = da.get('tel')
        session['arrive'] = da.get('arrive')
        session['arrivetime'] = da.get('arrivetime')
        session['ordernum1'] = da.get('ordernum1')
        # session['visit'] = da.get('visit')
        session.permanent = True
        handle_arrive_post(company=da.get('company'),
                           username=da.get('username'),
                            arrive=da.get('arrive'), arrivetime=da.get('arrivetime'),
                           ordernum1=da.get('ordernum1'))
        # handle_arrive_post(school=da.get('school'),company=da.get('company'),
        #             username=da.get('username'),work=da.get('work'),
        #             tel=da.get('tel'),arrive=da.get('arrive'),
        #             arrivetime=da.get('arrivetime'),ordernum1=da.get('ordernum1'),
        #             visit=da.get('visit'))
    elif request.data.get('num') == 2:
        pass


@app.route('/leave_handler')
def leave_handler():
    pass


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


if __name__ == "__main__":
    app.run()