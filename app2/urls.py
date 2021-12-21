from django.urls import path
from app2 import views

urlpatterns=[
    path('sample/',views.sample,name="sample"),
    path('home/',views.home,name="home"),
]