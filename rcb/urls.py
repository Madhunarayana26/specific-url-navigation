from django.urls import path
app_name='rcb'
from rcb.views import *
urlpatterns=[
    path('virat/',virat,name='virat'),
]