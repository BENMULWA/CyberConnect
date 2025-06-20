from django.shortcuts import render

def homepage(request):
    return render(request, 'homepage/home.html')

def know_more_view(request):
    return render(request, 'homepage/know_more.html')

def ecitizen_detail(request):
    return render(request, 'homepage/ecitizen_detail.html')