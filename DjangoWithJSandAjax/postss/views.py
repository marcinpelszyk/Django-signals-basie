from django.shortcuts import render
from django.http import JsonResponse
from .models import Post


def post_list_and_create(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'postss/main.html', context)

def hello(request):
    return JsonResponse({'text': 'hello białysto'})


