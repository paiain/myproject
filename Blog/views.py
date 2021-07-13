from django.shortcuts import render,HttpResponse

# Create your views here.
def index(reqest) :
    return HttpResponse("hello Django Framework")
