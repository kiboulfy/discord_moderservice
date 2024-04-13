from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.authen, name='index'),
    path('adding/', views.adding, name='adding'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('info/', views.info, name='info'),
    path('info/<int:pk>', views.info_detail, name = 'info-detail'),
    path('delete/<int:pk>', views.adding_delete, name = 'info-delete'),
]