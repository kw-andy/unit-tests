#from django.shortcuts import render p84/44

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# home_page = None p100/60

def home_page(request):
	if request.method == 'POST':
		return HttpResponse(request.POST['item_text'])
	return render(request,'home.html')	