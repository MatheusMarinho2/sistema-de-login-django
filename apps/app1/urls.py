from django.urls import path, include
from . import views
from .views import CustomPasswordChangeView

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path('registration/signup/', views.signup, name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('accounts/password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('', views.TaskListView.as_view(), name='task_list'),
    path('new/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
