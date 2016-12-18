# -*- coding: utf-8 -*-
import requests
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

import threading

from .forms import PushMessage

from sendserver import schedulerDATA
from sendserver import senddatatopic

def index(request):
	# 시간 설정후 보내기
	if request.method == 'POST' and 'withtime' in request.POST:
		form = PushMessage(request.POST)
		token = form.data['tokenid']
		body = form.data['body']
		title = form.data['title']
		time = form.data['time']
		t1 = threading.Thread(target=schedulerDATA,args=(token,body,title,time))
		t1.start()
		return render(request,'index2.html',{'form':form})
	# 시간 안 설정후 보내기
	elif request.method == 'POST' and 'withouttime' in request.POST:
		form = PushMessage(request.POST)
		token = form.data['tokenid']
		body = form.data['body']
		title = form.data['title']
		t1 = threading.Thread(target=schedulerDATA,args=(token,body,title,'without'))
		t1.start()
		return render(request,'index2.html',{'form':form})
	# 토픽 설정후 보내기
	elif request.method == 'POST' and 'topic' in request.POST:
		form = PushMessage(request.POST)
		body = form.data['body']
		title = form.data['title']
		topic = form.data['checkdata']
		t1 = threading.Thread(target=senddatatopic,args=(body,title,topic))
		t1.start()
		return render(request,'index2.html',{'form':form})		
	# 아무런 입력이 없는경
	else:
		form = PushMessage()

	return render(request,'index.html',{'form':form})
