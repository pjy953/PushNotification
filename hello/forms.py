from django.forms import ModelForm
from django import forms

class PushMessage(forms.Form):
	title = forms.CharField(max_length=30)
	body = forms.CharField(max_length=50)
	time = forms.TimeField()