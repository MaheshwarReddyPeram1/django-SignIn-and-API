from django.urls import path
from .import  views

urlpatterns=[
     path('chekingvalues',views.getCourse, name=''),
]