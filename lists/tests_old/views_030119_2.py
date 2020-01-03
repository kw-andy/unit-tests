#from django.shortcuts import render p84/44

#from django.http import HttpResponse
from django.shortcuts import render,redirect
from lists.models import Item

# Create your views here.

# home_page = None p100/60

def home_page(request):
	if request.method == 'POST':
		Item.objects.create(text=request.POST['item_text']) 
		return redirect('/')

	return render(request,'home.html')