# -*- coding: utf-8 -*-
from urllib2 import *
import urllib
import json
import sys
import gevent
import gevent.monkey
from datetime import datetime
gevent.monkey.patch_socket()
gevent.monkey.patch_ssl()

# topic 전송
def senddatatopic(body,title,topic):
    MY_API_KEY="AIzaSyBnItRBbhgV46AJMX2vT7QvnFst97H1R-Q"

    data={
        "to": "/topics/"+topic,
        "notification" : {
            "body" : body,
            "title" : title,
        }
    }

    dataAsJSON = json.dumps(data)

    request = Request(
        "https://gcm-http.googleapis.com/gcm/send",
        dataAsJSON,
        { "Authorization" : "key="+MY_API_KEY,
          "Content-type" : "application/json"
        }
    )
    urlopen(request)   

def senddata(tokens,body,title): 
    MY_API_KEY="AIzaSyBnItRBbhgV46AJMX2vT7QvnFst97H1R-Q"

    data={
        "registration_ids": tokens,
        "notification" : {
            "body" : body,
            "title" : title,
        }
    }

    dataAsJSON = json.dumps(data)

    request = Request(
        "https://gcm-http.googleapis.com/gcm/send",
        dataAsJSON,
        { "Authorization" : "key="+MY_API_KEY,
          "Content-type" : "application/json"
        }
    )
    urlopen(request)

def schedulerDATA(tokens,body,title,time):
    registrationGroup = []

    i = 1
    registration1000 = []
    for j in tokens:
        registration1000.append(j['regid'])
        i += 1
        if i == 1000:
            i = 0
            registrationGroup.append(registration1000)
            registration1000 = []
    registrationGroup.append(registration1000)

    # 예약전송을 위한 시간 계산
    if time == 'without':
        SleepSeconds = 0
    else:
        year = time[0:4]
        month = time[5:7]
        day = time[8:10]
        hour = time[11:13]
        minute = time[14:16]
        PushTime = datetime(int(year),int(month),int(day),int(hour),int(minute))
        NowTime = datetime.now()
        SleepTime = PushTime-NowTime
        SleepSeconds = SleepTime.days*60*60*24 + SleepTime.seconds
        if SleepSeconds < 0:
            SleepSeconds = 0

    # gevent를 이용한 비동기 처리
    LENGTH = len(registrationGroup)
    threads = []
    for i in range(0,LENGTH):
        threads.append(gevent.spawn_later(SleepSeconds,senddata,registrationGroup[i],body,title))
    gevent.joinall(threads)