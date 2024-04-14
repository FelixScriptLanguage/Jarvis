# -*- coding: utf-8 -*-
import os
import time

import pyttsx3
from flask import *
pyttsx3.init()

app = Flask(__name__)
Text = ''
tm = time.time()
man = False
speak = True
yanshi = 1.5
PID = ''
@app.route('/content', methods=['GET'])
def content():
    global Text,tm
    '''if time.time()-tm <= yanshi:
        tm = time.time()
        Text = request.args.get('content')
        return "ok"
    else:
        tm = time.time()
        Text = request.args.get('content')
        print()
        return "del"'''
    tm = time.time()
    Text = request.args.get('content')
    return 'ok'
@app.route('/del')
def Del():
    if time.time() - tm <= yanshi:
        return "ok"
    else:
        return "del"
@app.route('/text')
def getText():
    if time.time() - tm <= yanshi:
        return Text
    else:
        return ''
@app.route('/time')
def getTime():
    return time.time()-tm
@app.route('/cm')
def cm():
    global man
    man = not man
    ret, frame = cap.read()
    cv2.imwrite("temp/in/" + str(time.time()) + '.jpg', frame)
    if man:
        os.system('start /min client.lnk')
    else:
        pyttsx3.speak('Jarvis has been closed')
        os.system('taskkill /f /im '+PID)
    print(man)
    return 'ok'
@app.route('/pid', methods=['GET'])
def pid():
    global PID
    PID = request.args.get('pid')
    return 'ok'
@app.route('/speak')
def spk():
    global speak
    speak = not speak
    return 'speak'
@app.route('/canSpeak')
def canspk():
    return str(speak)
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5970)
    cap.release()