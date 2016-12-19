from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^message/$', hello.views.message, name='message'),
    url(r'^regist/$', hello.views.index, name='index')
]
