#from django.shortcuts import render p84/44

from django.shortcuts import render

# Create your views here.

# home_page = None p70/30

def home_page(request):
	return render(request,'home.html')