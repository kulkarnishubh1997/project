from django.shortcuts import render
from django.http import HttpResponse

def demo(request):
    return HttpResponse("Hello , how are you?")

def hello(request):
    data="""
    <html>
    <head><title>Hello</title></head>
    <body>
    <h1>Welcome to pyspider</h1>
    <marquee>thank you so much</marquee>
    </body></html>
    """
    return HttpResponse(data)

def helloDemo(request):
    data="""<html>
    <head><title>HelloDemo</title></head>
    <body>
    <h1>Welcome to Django</h1>
    <marquee>thank you so much</marquee>
    </body></html> """
    return HttpResponse(data)

def sample(request):
    fp=open(r"C:\Users\Shubhajinkya\Desktop\Django\Project1\pro1\sample.html")
    res=fp.read()
    fp.close()
    return HttpResponse(res)

def home(request):
    return render(request,'home.html')



