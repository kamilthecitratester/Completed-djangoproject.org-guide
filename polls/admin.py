from django.contrib import admin

from .models import Question

from .models import Choice, Question



admin.site.register(Choice)
admin.site.register(Question)
# Register your models here.
