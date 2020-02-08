from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class FeedPost(models.Model):
	title= models.CharField(max_length=50)
	content=models.TextField()
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=User.objects.get(username="Bhanu").id)
	published_date=models.DateTimeField(default=timezone.now)

	def __str__(self):
		return f'{self.title} by {self.author}'
