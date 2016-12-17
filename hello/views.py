import requests
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

import threading

from .forms import PushMessage

from sendserver import schedulerDATA

def index(request):
	if request.method == 'POST' and 'withtime' in request.POST:
		form = PushMessage(request.POST)
		body = form.data['body']
		title = form.data['title']
		time = form.data['time']
		t1 = threading.Thread(target=schedulerDATA,args=(body,title,time))
		t1.start()
		return render(request,'index2.html',{'form':form})
	elif request.method == 'POST' and 'withouttime' in request.POST:
		form = PushMessage(request.POST)
		body = form.data['body']
		title = form.data['title']
		t1 = threading.Thread(target=schedulerDATA,args=(body,title,'without'))
		t1.start()
		return render(request,'index2.html',{'form':form})
	else:
		form = PushMessage()

	return render(request,'index.html',{'form':form})
