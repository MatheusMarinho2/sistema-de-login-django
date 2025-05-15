from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'A Fazer'),
        ('doing', 'Fazendo'),
        ('done', 'Concluída'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(User, related_name='tasks_created', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks_assigned', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True, blank=True)

    class Meta:
        permissions = [
            ("can_view_all_tasks", "Pode ver todas as tarefas"),
            ("can_manage_tasks", "Pode criar/editar/excluir todas as tarefas"),
        ]

    def __str__(self):
        return self.title
