from django.urls import path
from scraper import views

app_name = 'scraper'

urlpatterns = [
    path('', views.index, name="index"),
    path('extract_emails', views.extract_email_ajax, name="extract_emails"),
]