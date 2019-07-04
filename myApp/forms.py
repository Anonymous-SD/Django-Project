from django import forms
from django.core import validators


class MyForm(forms.Form):




	def check_text_length(value):
		if len(value) > 20:

			raise forms.ValidationError('Text length exceeded')
		

	name 	= forms.CharField(validators = [validators.MaxLengthValidator(20)])
	email 	= forms.EmailField()
	confirm_email = forms.EmailField(label = 'Confirm Email')
	text 	= forms.CharField(widget = forms.Textarea, validators = [check_text_length])
	botcatcher = forms.CharField(widget = forms.HiddenInput, required = False)

	def clean_botcatcher(self):

		clean_botcatcher = self.cleaned_data['botcatcher']

		if len(clean_botcatcher) > 0:

			raise forms.ValidationError('GOTCHA BOT!!')

		return clean_botcatcher

	def clean(self):

		all_clean_data = super().clean()

		print(all_clean_data)

		if all_clean_data['email'] != all_clean_data['confirm_email']:

			raise forms.ValidationError('Emails do not match')

