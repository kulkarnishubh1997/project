from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def sample(request):
    return HttpResponse("this is app1")

def home(request):
    return render(request,'app1_home.html')

def index(request,data):
    return HttpResponse("<h1>hii Mrs. {} </h1>".format(data))
