from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return HttpResponse('This is the Tool Overview Page.')

