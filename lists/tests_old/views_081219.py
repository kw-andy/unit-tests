#from django.shortcuts import render p72/32

from django.http import HttpResponse

# Create your views here.

# home_page = None p70/30

def home_page(request):
	return HttpResponse('<html><title>To-Do lists</title></html>')