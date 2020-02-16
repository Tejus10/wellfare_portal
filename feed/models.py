from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
# Create your models here.


class Message(models.Model):
	title= models.CharField(max_length=50)
	subtitle=models.TextField(null=True)
	content=models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, null=True,on_delete=models.SET_NULL)
	published_date=models.DateTimeField(default=timezone.now)

	def _str_(self):
		return f'{self.title} by {self.author}'

class Post(models.Model):
	author= models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
	photo=models.ImageField(upload_to='images/')
	caption=models.TextField(blank=True)
	published_date=models.DateTimeField(default=timezone.now)

	def _str_(self):
		return f'{self.author}\'s post'

class announcements(models.Model):
	content = models.TextField()
	published_date = models.DateTimeField(default=timezone.now)
	


class about(models.Model):
	content = models.TextField()
	def _str_(self):
		return f'{self.content}'

class faq(models.Model):
	question = models.TextField()
	answer = models.TextField()
	def _str_(self):
		return f'{self.question}'

class counsellor_timing(models.Model):
	timings = models.TextField(null=True)

class counsellor(models.Model):
	name = models.CharField(max_length=70)
	photo = models.ImageField(upload_to='images/',null=True)
	about = models.TextField()
	timings = models.TextField(null=True,blank = True)
	contact = models.TextField(null=True,blank = True)
	def _str_(self):
		return f'{self.name}'


	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)

		if img.height > 400 or img.width > 400:
			output_size = (400, 400)
			img.thumbnail(output_size)
			img.save(self.photo.path)	
	

class psychiatrist(models.Model):
	name = models.CharField(max_length=70)
	photo = models.ImageField(upload_to='images/',null=True)
	about = models.TextField()
	contact = models.TextField(null=True,blank = True)
	def _str_(self):
		return f'{self.name}'

class chairman(models.Model):
	name = models.CharField(max_length=70)
	photo = models.ImageField(upload_to='images/',null=True)
	about = models.TextField()
	contact = models.TextField(null=True,blank = True)
	def _str_(self):
		return f'{self.name}'


class gallery(models.Model):
	photo = models.ImageField(upload_to='images/',null=True)
	video = models.FileField(upload_to='videos/',null=True)

class activities(models.Model):
	title = models.CharField(max_length=150)
	content = models.TextField()
	photo  = models.ImageField(upload_to='images/',null=True)
	def _str_(self):
		return f'{self.title}'	

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.photo.path)

		if img.height > 400 or img.width > 400:
			output_size = (400, 400)
			img.thumbnail(output_size)
			img.save(self.photo.path)	