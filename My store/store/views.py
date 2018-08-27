from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
# from .models import *

# Create your views here.
def home(request):
	return render(request, 'home.html')
	
# def home(request):
# 	return render(request, 'home.html', locals())
