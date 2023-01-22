from django.contrib import admin
from .models import Journal


# В этой части регистрируем модели.
admin.site.register(Journal)
