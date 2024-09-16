from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home_page, name="home_page"),
    path('home/<int:pk>', views.delete_em, name="delete_em" )
]