from django.contrib import admin
from django.urls import path
from .views import calculos
urlpatterns = [path("admin/", admin.site.urls), path("async/", calculos, name="calculos")]
