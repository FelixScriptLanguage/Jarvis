import random
import easygui
import pyttsx3
import requests
import os
import time
from pygame import mixer

mixer.init()
pyttsx3.init()

text = ''
noTip = False
role = ''
task = ''
Record = ''
def getDir(path):
    for root,dirs,files in os.walk(path):
        return dirs
def speak(text,sound):
    try:
        if os.path.isfile('./content.mp3'):
            os.remove('./content.mp3')
        open('content.txt','w',encoding='utf-8').write(text)
        os.system(r'edge-tts.exe'+' -f "content.txt" --write-media "content.mp3" --voice '+sound)
        mixer.init()
        mixer.music.load(r"./content.mp3")
        mixer.music.play()
        while mixer.music.get_busy():
            time.sleep(0.5)
        mixer.quit()
    except Exception as a:
        print(a)
        pyttsx3.speak(text)
#engine = pyttsx3.init()
while True:
    try:
        content = requests.get('http://127.0.0.1:5970/text').text
        if content == '':
            if text == '':
                continue
            if [i for i in
                          ['贾维斯', '蕾丝', '维斯', '詹文斯', '没斯', '白丝', '梅斯', '蒋欣', '小微生', '我一思', '维思', '没丝',
                           '好一思', '梅丝', 'jervis', 'jeris', 'jewis', 'jerris', 'jerous','莱斯','没事，','维丝','白斯','学思'] if
                          i in text] or (noTip and role == '贾维斯'):
                record = [i for i in
                          ['贾维斯', '蕾丝', '维斯', '詹文斯', '没斯', '白丝', '梅斯', '蒋欣', '小微生', '我一思', '维思', '没丝',
                           '好一思', '梅丝', 'jervis', 'jeris', 'jewis', 'jerris', 'jerous','莱斯','没事，','维丝','白斯','学思'] if
                          i in text]
                role = '贾维斯'
                if not noTip:
                    List = []
                    for i in record:
                        List.append(len(text.split(i)[0]))
                    ls = min(List)
                    rcd = ''
                    num = 0
                    for i in List:
                        if ls == i:
                            rcd = record[num]
                        num += 1
                    text = rcd.join(text.split(rcd)[1:])
                if text.replace(' ','') == '':
                    continue
                if text[0] == ',' or text[0] == '，':
                    text = text[1:]
                print('\a')
                requests.get('http://127.0.0.1:5970/speak')
                print('我说：', text)
                print('start answer')
                t = chatgpt('请你模仿钢铁侠中的贾维斯，现在我说：'+text)
                print('贾维斯说：',t)
                speak(t,'zh-CN-YunyangNeural')
                text = ''
                print('\a')
                requests.get('http://127.0.0.1:5970/speak')
        else:
            text = content
        time.sleep(2)
        os.system('cls')
    except Exception as a:
        print('error',a)