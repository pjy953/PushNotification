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

# def fetch(request):
#     urlopen(request)


def senddata(body,title):
# def senddata(body,title,registrationids):
    MY_API_KEY="AIzaSyBnItRBbhgV46AJMX2vT7QvnFst97H1R-Q"

    data={
        "registration_ids": ['fqbB0SFg2Pw:APA91bFHB1w3E108RCR1Nlw-64N4uUklbtVNE6-S9xJkXQ8JJygIql6zEkGKSdvBvNQ2v7UVOkGXGS7RaNi6iNkYCgYQFaoNnOQm8Asj_EQsNUzg291TtfLAI4xWwxdPfx_wTb9kHw0c'],
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
    # print urlopen(request).read()


    # data={
    #     "registration_ids": registrationids,
    #     "notification" : {
    #         "body" : body,
    #         "title" : title,
    #     }
    # }

    # dataAsJSON = json.dumps(data)

    # request = Request(
    #     "https://gcm-http.googleapis.com/gcm/send",
    #     dataAsJSON,
    #     { "Authorization" : "key="+ MY_API_KEY,
    #       "Content-type" : "application/json"
    #     }
    # )
    # urlopen(request)

def schedulerDATA(body,title,time):
    # # 데이터베이스에서 레지스트레이션 아이디를 가지고옴
    # # registrationGroups에 보관
    # registrationGroup = []
    # for j in registrationGroups:
    #     registration1000 = []
    #     for i in xrange(0,1000):
    #         registration1000.append(j)
    #     registrationGroup.append(registration1000)
    # # registrationGroup에는 1000개단위의 레지스트레이션 아이디의 묶음이 존재

    # 예약전송을 위한 시간 계산
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
    # senddata(body,title,registrationGroup)
    # LENGTH = len(registrationGroup)
    LENGTH = 2
    threads = []
    for i in range(0,LENGTH):
        threads.append(gevent.spawn_later(SleepSeconds,senddata,body,title))
        # threads.append(gevent.spawn(senddata,body,title,registrationGroup[i]))
    gevent.joinall(threads)