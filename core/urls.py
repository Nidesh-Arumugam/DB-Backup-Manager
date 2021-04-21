from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from   core import views


urlpatterns=[
    path('',views.index, name='homepage'),
    path('detail/', views.database_detail_view, name='detailpage' ),
    path('api/', views.TestView.as_view(), name='test'),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token', obtain_auth_token, name='obtain-token'),
    path('rest-auth/', include('rest_auth.urls')),
    path('detail/display/', views.ListOfDatabase, name='databaselist'),
    


]