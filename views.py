from django.http import HttpResponse
from django.shortcuts import redirect
import numpy
import pandas

def index(request):
    return HttpResponse('index')

def login(request):
    return redirect('/index')
