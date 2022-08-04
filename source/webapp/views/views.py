from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView


def index_view(request):

    return render(request, 'index.html')