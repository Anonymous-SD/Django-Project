from django.db import models

# Create your models here.

class userModel(models.Model):

	FirstName 		= models.CharField(max_length = 30)
	LastName 		= models.CharField(max_length = 30)
	Email 			= models.EmailField(max_length = 50, unique = True)


	def __str__(self):
		return self.FirstName +' '+self.LastName
