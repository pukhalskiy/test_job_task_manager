from django.db import models


class Task(models.Model):
    STATUS_CHOICES = [
        ('pending', 'В очереди'),
        ('in_progress', 'В процессе'),
        ('completed', 'Завершена'),
    ]

    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=50,
                              choices=STATUS_CHOICES,
                              default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
