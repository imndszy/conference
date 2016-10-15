# -*- coding:utf8 -*-
# Author: shizhenyu96@gamil.com
# github: https://github.com/imndszy
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import hashlib
from flask import Flask, request, make_response, render_template, session, jsonify

from app.config import TOKEN
from app.handler import handle_arrive_post

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'asdasdasdadadada'


@app.route('/', methods=['GET'])
def wechat_auth():
    echostr = request.args.get('echostr', '')
    if verification():
        return make_response(echostr)
    return 'render_template("index.html")'


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/arrive')
def arrive():
    return render_template('Arrive.html')


@app.route('/leave')
def leave():
    return render_template('Leave.html')


@app.route('/arrive_post',methods=['POST'])
def arrive_post():
    da = request.values
    session['school'] = da.get('school').encode('utf8')
    session['company'] = da.get('company').encode('utf8')
    session['username'] = da.get('username').encode('utf8')
    session['work'] = da.get('work').encode('utf8')
    session['tel'] = da.get('tel').encode('utf8')
    session['arrive'] = da.get('arrive').encode('utf8')
    session['arrivetime'] = da.get('arrivetime').encode('utf8')
    session['ordernum1'] = da.get('ordernum1').encode('utf8')
    session['visit'] = da.get('visit').encode('utf8')
    session['leave'] = '-1'
    session['leavetime'] = 'unknown'
    session['ordernum2'] = 'unknown'
    session.permanent = True
    print handle_arrive_post(school=session['school'],company=session['company'],
                username=session['username'],work=session['work'],
                tel=session['tel'],arrive=session['arrive'],
                arrivetime=session['arrivetime'],ordernum1=session['ordernum1'],
                visit=session['visit'],leave=session['leave'],leavetime=session['leavetime'],
                ordernum2=session['ordernum2'])
    return 'ad'


@app.route('/arrive_get')
def arrive_get():
    return jsonify(company='asd', username='asd',
                   school='sad', work='asd', tel='123',
                   arrive='1', ordernum='63546', arrivetime='2016-10-20-10:20')

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


if __name__ == "__main__":
    app.run()