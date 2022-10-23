from django.contrib import admin
from django.urls import path, include

from scraper import views

urlpatterns = [
    path('', views.index, name="index"),
    path('scraper/', include('scraper.urls')),
    path('admin/', admin.site.urls),
]
