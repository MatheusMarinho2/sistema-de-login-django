from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home.as_view(), name='home'),
    path('registration/signup/', views.signup, name='signup'),  
    path("accounts/", include("django.contrib.auth.urls")), 
]
