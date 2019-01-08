from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import SubjectPost, Post


def get_base_menu(data):
    data['subjects'] = SubjectPost.objects.all()


def post_list(request):
    data = {}
    get_base_menu(data)
    data['posts'] = Post.objects.filter(status='y', published_date__lte=timezone.now()).order_by('-published_date')[:2]
    return render(request, 'blog/post_list.html', data)


def subject_detail(request, url):
    data = {}
    get_base_menu(data)
    data["subject"] = get_object_or_404(SubjectPost, url=url)
    return render(request, 'blog/subject_detail.html', data)


def blog_subject_all(request):
    data = {}
    get_base_menu(data)
    data['subject'] = SubjectPost.objects.all()
    return render(request, 'blog/blog_subject_all.html', data)


def post_detail(request, post):
    data = {}
    get_base_menu(data)
    data['post'] = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post_detail.html', data)


def blog_post_all(request):
    data = {}
    get_base_menu(data)
    data['posts'] = Post.objects.all()
    return render(request, 'blog/blog_post_all.html', data)

