from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class App(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	
class AppUser(models.Model):
	user = models.ForeignKey(User)
	app = models.ForeignKey(App)