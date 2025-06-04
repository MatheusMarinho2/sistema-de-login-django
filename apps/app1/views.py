from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Task
from django.contrib.auth.views import PasswordChangeView
from .forms import CustomPasswordChangeForm


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = '/accounts/password_change/done/'


class home(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.has_perm('app1.can_view_all_tasks'):
            return qs

        return qs.filter(Q(created_by=user) | Q(assigned_to=user))


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Task
    template_name = 'task_form.html'
    fields = ['title', 'description', 'status', 'assigned_to', 'due_date']
    permission_required = 'app1.can_manage_tasks'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Task
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    fields = ['title','description','assigned_to','status','due_date']
    permission_required = 'app1.can_manage_tasks'


class TaskDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task_list')
    permission_required = 'app1.can_manage_tasks'
