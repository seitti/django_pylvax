import json
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import JsonResponse


def home(request):
    home_data = Post.objects.all().order_by('created_date')

    for item in home_data:
        item.text = item.text[:80] + '...'

    context_dict = {'posts': home_data}

    return render(request, 'starter_app/home.html', context_dict)


def post(request, slug):
    get_post = get_object_or_404(Post, slug=slug)
    home_data = Post.objects.all()
    context_dict = {'selected_post': get_post,
                    'posts': home_data}

    return render(request, 'starter_app/post.html', context_dict)
