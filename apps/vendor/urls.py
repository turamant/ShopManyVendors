from django.urls import path
from django.contrib.auth import views as auth_views
from apps.vendor import views


urlpatterns = [
    path('become-vendor/', views.become_vendor, name='become_vendor'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html'), name='login'),
]