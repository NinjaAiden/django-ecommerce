from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    """
    A view that displays the index page
    """
    return redirect(request, "index.html")