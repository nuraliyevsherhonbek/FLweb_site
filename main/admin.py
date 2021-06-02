from django.contrib import admin
from .models import Course, Event, Result, Application, SocialNetwork, StudentNumber


admin.site.register(Course)
admin.site.register(Event)
admin.site.register(Result)
admin.site.register(Application)
admin.site.register(SocialNetwork)
admin.site.register(StudentNumber)
