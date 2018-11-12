from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def main_dashboard(request, *args, **kwargs):
    print(args, kwargs) # request to know user 
    print(request.user) # knowing user who accesed the page 
    # return HttpResponse("Welcome to my blog dashboard") 
    return render (request, "base.html", {})

def post(request, *args, **kwargs):
    print(args, kwargs) # request to know user 
    print(request.user) # knowing user who accesed the page 
    # return HttpResponse("Welcome to my blog dashboard") 
    return render (request, "post.html", {})
