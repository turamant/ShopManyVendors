from django.urls import path

from apps.vendor import views


urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
]