from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(requests):
    blogs = Blog.objects.all().order_by('-date')
    return render(requests, "blog/all_blogs.html", {'blogs': blogs})


def detail(requests, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(requests, 'blog/detail.html', {'blog': blog})