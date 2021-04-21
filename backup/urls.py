
from django.contrib import admin
from django.urls import path, include
from core.views import TestView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('',include('core.urls')),
    path('admin/', admin.site.urls),
    
]

