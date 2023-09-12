from django.shortcuts import render

def index (request):
    return render(request, "home.html")

def index_about (request):
    return render(request, "about.html")
# Create your views here.
def index_base (request):
    return render(request, "base.html")
