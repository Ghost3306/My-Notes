from django.urls import path
from accounts import views

urlpatterns = [
    path('login',views.login_user),
    path('register',views.register),
    path('activate/<uuid>/',views.activate_profile),
    path('logout',views.logout_user)
]
