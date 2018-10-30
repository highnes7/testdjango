
from django.shortcuts import render
from django.http import HttpResponse
from .models import posts


def index(request):

 post = posts.objects.all()[:10]

 context = {
     'title' : 'Latest Posts' ,
    'posts' : post
    }    
 return render(request, 'posts/index.html',context)



def details(request, id):
 post = posts.objects.get(id=id)

 context = {
            'post': post
    }
 return render(request, 'posts/details.html',context)       