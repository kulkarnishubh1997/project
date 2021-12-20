from django.urls import path
from app1 import views
urlpatterns=[
    path('sample/',views.sample,name="sample"),
]