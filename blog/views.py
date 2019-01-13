from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse
from blog.models import SubjectPost, Post

def post_list(request):
    data = {}
    data['posts'] = Post.objects.filter(status='y', published_date__lte=timezone.now()).order_by('-published_date')[:2]
    return render(request, 'blog/post_list.html', data)


def subject_detail(request, url):
    data = {}
    data["subject"] = get_object_or_404(SubjectPost, url=url)
    return render(request, 'blog/subject_detail.html', data)


def blog_subject_all(request):
    data = {}
    data['subject'] = SubjectPost.objects.all()
    return render(request, 'blog/blog_subject_all.html', data)


def post_detail(request, post):
    data = {}
    data['post'] = get_object_or_404(Post, slug=post)
    return render(request, 'blog/post_detail.html', data)


def blog_post_all(request):
    data = {}
    data['posts'] = Post.objects.all()
    return render(request, 'blog/blog_post_all.html', data)

def get_subjects(request):

    subjects = list(map(lambda post: post.subject, SubjectPost.objects.all()))

    """

    subjects = []

    for post in SubjectPost.objects.all():

        subjects.append(post.subject)

    """

    # В JS: json.subjects или json["subjects"]
    return JsonResponse({ "subjects" : subjects })
