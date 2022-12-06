from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
# Create your views here.

def simple_view(request):
    return render(request,'first_app/example.html')