from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Merhaba")


def blogpage(request):
    return HttpResponse("Bu blog sayfası çok güzeldir.")