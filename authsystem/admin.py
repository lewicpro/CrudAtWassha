from django.contrib import admin
from .models import *

# Register your models here.

class NamesAdmin(admin.ModelAdmin):
    list_display=[
        'user',
        'name',
        'email',
        'year',
    ]

admin.site.register(NamesModel, NamesAdmin)