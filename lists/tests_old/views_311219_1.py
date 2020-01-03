#from django.shortcuts import render p84/44

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# home_page = None p100/60

def home_page(request):
	
	item = item()
	item.text = request.POST.get('item_text','')
	item.save()

	return render(request,'home.html',{
		'new_item_text': item.text,
	})	