from django.shortcuts import render
from .models import Message,Post

# Create your views here.
def homepage(request):
	messages= Message.objects.all().order_by("-published_date")
	posts=Post.objects.all().order_by("-published_date")
	context={'messages':messages, 'posts':posts}
	return render(request,"feed/index.html",context)