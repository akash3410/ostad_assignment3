from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name="account_home"),
    path('registration/', views.registration, name="registration"),
    path('login/', views.login_view, name = "login_view")
]