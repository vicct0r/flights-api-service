
from django.contrib import admin
from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('flights.urls')),
    re_path('login', views.login),
    re_path('signup', views.signup),
    re_path('test_token', views.test_token),
]
