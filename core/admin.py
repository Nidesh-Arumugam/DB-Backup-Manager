from django.contrib import admin
from .models import databases,DatabaseAdmin
# Register your models here.

admin.site.register(databases, DatabaseAdmin)
