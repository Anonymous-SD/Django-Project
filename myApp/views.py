from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from myApp.models import AccessRecord, Topic, WebPage

# Create your views here.

def index(request):

	access_records = AccessRecord.objects.order_by('date')

	context = {
	'access_records': access_records,
	'my_title': 'App Index'
	}

	return render(request, 'myApp/index.html', context)


def formView(request):

	form = forms.MyForm()

	context = {
	'form' : form
	}

	return render(request, 'myApp/form.html', context)
