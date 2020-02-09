from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Message(models.Model):
	title= models.CharField(max_length=50)
	subtitle=models.TextField(null=True)
	content=models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
	published_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.title} by {self.author}'

class Post(models.Model):
	author= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
	photo=models.ImageField(upload_to='images/')
	caption=models.TextField(blank=True)
	published_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.author}\'s post'