from django.shortcuts import render
from .models import *

# Create your views here.
def homepage(request):
	messages= Message.objects.all().order_by("-published_date")
	posts=Post.objects.all().order_by("-published_date")
	abouts=about.objects.all()
	faqs=faq.objects.all()
	psychiatrists=psychiatrist.objects.all()
	chairmans=chairman.objects.all()
	gallerys=gallery.objects.all()
	announcementss=announcements.objects.all()
	activitiess=activities.objects.all()
	counsellor_timings=counsellor_timing.objects.get(pk=1)
	context={'messages':messages, 
			'posts':posts,
			'about':abouts,
			'faqs':faqs,
			'psychiatrists':psychiatrists,
			'chairmans':chairmans,
			'gallerys':gallerys,
			'announcementss':announcementss,
			'activitiess':activitiess,
			'counsellor_timings':counsellor_timings,
			}
	return render(request,"feed/index.html",context)


def activity(request):
	activitiess=activities.objects.all()
	context={
			'activitiess':activitiess,
			}	
	return render(request,"feed/activities.html",context)


def team(request):
	counsellors=counsellor.objects.all()
	psychiatrists=psychiatrist.objects.all()
	chairmans=chairman.objects.all()
	counsellor_timings=counsellor_timing.objects.get(pk=1)	
	context={'counsellors':counsellors,
			'psychiatrists':psychiatrists,
			'chairmans':chairmans,
			'counsellor_timings':counsellor_timings,
			}
	return render(request,"feed/team.html",context)		


def gall(request):	
	gallerys=gallery.objects.all()
	context={
			'gallerys':gallerys,
			}
	return render(request,"feed/gallery.html",context)		