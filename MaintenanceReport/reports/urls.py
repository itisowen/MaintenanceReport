from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.my_register, name='register')
]
