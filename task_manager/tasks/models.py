from django.db import models

from core.constants import TITLE_LENGTH, STATUS_LENGTH

class Task(models.Model):
    """
    Модель Django для представления задачи.
    """
    STATUS_CHOICES = [
        ('pending', 'В очереди'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    title = models.CharField(max_length=TITLE_LENGTH, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=STATUS_LENGTH,
                              choices=STATUS_CHOICES,
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
