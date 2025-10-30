from django.shortcuts import render
from django.http import HttpResponse

from django.db.models import Q

from .models import Post

# Create your views here.

def find_post (request):

    query = request.GET.get ('search')

    if query:

        postModel = Post.objects.filter(

            Title__icontains=query

        )

        

    else:

        postModel = Post.objects.all()

    context = {
        'post' : postModel,
        'query' : query
    }

    return render (request, 'index.html', context=context)