from django.contrib import admin
from myApp.models import AccessRecord, Topic, WebPage

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)