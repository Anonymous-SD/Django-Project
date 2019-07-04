from django.conf.urls import url
from myApp import views


urlpatterns = [

	url(r'^$', views.index, name = 'index'),

	url(r'^myForm/$', views.formView, name= 'form')

]