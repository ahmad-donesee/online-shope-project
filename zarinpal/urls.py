from django.urls import path

app_name="zarinpal"

from . import views

urlpatterns = [
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
]
