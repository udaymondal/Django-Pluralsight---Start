from django.contrib import admin

# Register your models here.

from .models import Meeting, Person

admin.site.register(Meeting)
admin.site.register(Person)