from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('register/', views.my_register, name='register'),
    path('reportform/', views.report_form, name='reportform'),
    path('login/', views.my_login, name='login'),
    path('detail/<int:maintenance_id>', views.detail, name='detail'),
    path('logout/', views.my_logout, name='logout')
]
