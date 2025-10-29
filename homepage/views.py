from django.shortcuts import render, get_object_or_404
from django.core import signing
from .models import BlogPost


def homepage(request):
    return render(request, 'homepage/home.html')

def review_detail(request, token):
    try:
        post_id = signing.loads(token)
        post = get_object_or_404(BlogPost, id=post_id)
    except signing.BadSignature:
        return render(request, '404.html', status=404)

    return render(request, 'homepage/review.html', {'post': post})



def about_view(request):
    return render(request, 'homepage/about.html')

def services_view(request):
    return render(request, 'homepage/home.html')

def careers_view(request):
    return render(request, 'homepage/home.html')


def know_more_view(request):
    return render(request, 'homepage/know_more.html')

def ecitizen_detail(request):
    return render(request, 'homepage/ecitizen_detail.html')