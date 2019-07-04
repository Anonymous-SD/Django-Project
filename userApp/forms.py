from . import models
from django import forms


class myForm(forms.ModelForm):
	class Meta():
		model 	= models.userModel
		fields 	= '__all__'
