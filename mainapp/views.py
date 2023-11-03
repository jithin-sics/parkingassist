from django import contrib
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.


def Home(request):
    return render(request,"base.html")

def features(request):
    return render(request,"dummy.html")