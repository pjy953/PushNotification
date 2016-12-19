# -*- coding: utf-8 -*-
import requests
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

import threading

from .forms import PushMessage
from .forms import Regid

from .models import Registrationid

from sendserver import schedulerDATA
from sendserver import senddatatopic

def index(request):
	# 시간 설정후 보내기
	if request.method == 'POST' and 'saveregid' in request.POST:
		form = Regid(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'regist.html',{'form':form})

	elif request.method == 'POST' and 'directmessage' in request.POST:
		return redirect('/message/')

	else:
		form = Regid()

	return render(request,'main.html',{'form':form})

def message(request):
	tokens = Registrationid.objects.all().values('regid').distinct()

	if request.method == 'POST' and 'withtime' in request.POST:
		form = PushMessage(request.POST)
		body = form.data['body']
		title = form.data['title']
		time = form.data['time']
		t1 = threading.Thread(target=schedulerDATA,args=(tokens,body,title,time))
		t1.start()
		return render(request,'index2.html',{'form':form})
	# 시간 안 설정후 보내기
	elif request.method == 'POST' and 'withouttime' in request.POST:
		form = PushMessage(request.POST)
		body = form.data['body']
		title = form.data['title']
		t1 = threading.Thread(target=schedulerDATA,args=(tokens,body,title,'without'))
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
	elif request.method == 'POST' and 'back' in request.POST:
		return redirect('../')	
	# 아무런 입력이 없는경우
	else:
		form = PushMessage()

	return render(request,'index.html',{'form':form})