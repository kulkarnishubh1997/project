from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sample(request):
    return HttpResponse("this is app2")

def home(request):
    return render(request,'app2_home.html')

