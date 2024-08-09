from django.contrib import admin
from django.urls import path,include
from notes import views
urlpatterns = [
    path('',views.homepage)
]
