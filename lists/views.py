from django.shortcuts import render
from django.http import  HttpResponse

def home_view(request):
    return render(request, 'lists/home.html', { 'item_text': request.POST.get('item_text','')})
