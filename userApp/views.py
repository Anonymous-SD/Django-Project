from django.shortcuts import render
from . import forms

# Create your views here.


def indexView(request):

	return render(request, 'userApp/index.html')


def signUpView(request):

	form = forms.myForm()

	if request.method == 'POST':
		form = forms.myForm(request.POST)

		if form.is_valid():
			form.save(commit = True)
			return indexView(request)

	context = {
	'form' : form
	}

	return render(request, 'userApp/signup.html', context)