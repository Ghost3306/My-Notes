from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.


def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
