from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import *

class DateInput(forms.DateInput):
	input_type = 'date'

class Self_help(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
			'photo',
			'caption',
			'published_date',
        ]
        widgets = {
            'published_date': DateInput(),
            
        }

class activities_form(forms.ModelForm):
    class Meta:
    	model = activities
    	fields = [
        	'title',
			'content',
			'photo',
        ]
        