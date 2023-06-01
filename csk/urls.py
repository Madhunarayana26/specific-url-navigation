from django.urls import path
app_name='csk'
from csk.views import *
urlpatterns=[
    path('dhoni/',dhoni,name='dhoni'),
]