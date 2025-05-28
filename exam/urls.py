from django.urls import path
from .views import smexam_list

urlpatterns = [
    path('smexam/', smexam_list, name='smexam_list'),
]