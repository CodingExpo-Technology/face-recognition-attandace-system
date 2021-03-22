from django.urls import path

from personal.views import (
    personal_dashboard_view,
)

urlpatterns=[
    path('personal_dashboard/',personal_dashboard_view, name='personal_dashboard')
]