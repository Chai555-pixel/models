# blog/views.py
from django.shortcuts import render

# This is the view that renders the home page
def home(request):
    return render(request, 'home.html')  # This renders the 'home.html' template
