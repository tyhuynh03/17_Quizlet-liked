# Register your models here.
from django.contrib import admin

from .models import User
from quiz.models import Topic
from quiz.models import Question



admin.site.register(User)
admin.site.register(Topic)
admin.site.register(Question)
