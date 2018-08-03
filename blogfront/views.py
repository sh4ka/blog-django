from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def index(request):
    posts = Post.objects.all().order_by('-pub_date').filter(published=True)[:5]
    return render(request, 'posts/index.html', {'posts': posts})


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.published == True:
        return render(request, 'posts/detail.html', {'post': post})
    raise Http404