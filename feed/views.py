from django.shortcuts import render
from .models import FeedPost

# Create your views here.
def homepage(request):
	posts= FeedPost.objects.all()
	context={'posts':posts}
	return render(request,"feed/index.html",context)