from django.shortcuts import render
from django.http import HttpResponse
from .models import post
from django.utils import timezone

def index(request):
    return HttpResponse('Welcome to the bloggy app')

def post_list(request):
    posts = post.objects.filter(publishedDate__lte=timezone.now()).order_by('publishedDate')
    return render(request, 'bloggy/post_list.html', {'posts': posts})
# Create your views here.
