from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Welcome to the bloggy app')

def post_list(request):
    return render(request, 'bloggy/post_list.html', {})
# Create your views here.
