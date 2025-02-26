import datetime

from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.objects.order_by(
        '-created_at'
    ).filter(
        pub_date__lte=datetime.datetime.now(),
        is_published=True,
        category__is_published=True
    )[:5]
    context = {
        'post_list': post_list
    }
    return render(request, template_name, context)


def post_detail(request, id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.datetime.now()
    )
    context = {
        'post': post
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    post_list = Post.objects.filter(
        category__slug=category_slug,
        is_published=True,
        pub_date__lte=datetime.datetime.now()
    )
    context = {
        'category': category,
        'post_list': post_list
    }
    return render(request, template_name, context)
