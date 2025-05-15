from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path('registration/signup/', views.signup, name='signup'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', views.TaskListView.as_view(), name='task_list'),
    path('new/', views.TaskCreateView.as_view(), name='task_create'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('<int:pk>/edit/', views.TaskUpdateView.as_view(), name='task_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='task_delete'),
]
