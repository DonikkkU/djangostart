from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'blog/home.html')
def test1(request):
    return render(request, 'blog/test1.html')
def test2(request):
    return render(request, 'blog/test2.html')
def test3(request):
    return render(request, 'blog/test3.html')