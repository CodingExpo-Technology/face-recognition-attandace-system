from django.shortcuts import render

# Create your views here.

def personal_dashboard_view(request):

    return render(request, 'personal/dashboard.html')