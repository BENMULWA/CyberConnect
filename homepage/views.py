from django.shortcuts import render

def homepage(request):
    from .models import BlogPost 
    posts = BlogPost.objects.all()  # Fetch all blog posts
    return render(request, "blog/home.html", {"posts": posts})
