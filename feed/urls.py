from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.homepage,name='home'),
	path('activities/',views.activity,name='activity'),
	path('team/',views.team,name='team'),
	path('gallery/',views.gall,name='gallery'),
	path('add_post/',views.self_help,name='add_post'),
    path('add_activity/',views.activity_add,name='add_activity'),
]