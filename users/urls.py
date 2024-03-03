from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup/', views.registerUser, name='signup'),
    path('profile/', views.profile, name='profile'),
]