from django.conf.urls import url
from userApp import views

app_name = 'userApp'

urlpatterns = [

url(r'^$', views.indexView, name ='index'),

url(r'^signup/$', views.signUpView, name = 'userSignUp')

]