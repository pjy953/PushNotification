from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)

class Registrationid(models.Model):
	regid = models.CharField(max_length=300)