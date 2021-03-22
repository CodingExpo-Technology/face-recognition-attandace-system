from typing import ContextManager
from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {}
    return render(request, 'main_website/index.html', context)

def user_view(request):
    context = {}
    return render(request, 'main_website/user.html', context)
