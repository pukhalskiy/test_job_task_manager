from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django_elasticsearch_dsl.registries import registry


@receiver(post_save)
def update_document(sender, **kwargs):
    """
    Обработчик сигнала post_save для обновления документа Elasticsearch
    при сохранении объекта модели.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'tasks':
        if model_name == 'task':
            instances = instance.article.all()
            for _instance in instances:
                registry.update(_instance)


@receiver(post_delete)
def delete_document(sender, **kwargs):
    """
    Обработчик сигнала post_delete для удаления документа Elasticsearch
    при удалении объекта модели.
    """
    app_label = sender._meta.app_label
    model_name = sender._meta.model_name
    instance = kwargs['instance']

    if app_label == 'tasks':
        if model_name == 'task':
            instances = instance.article.all()
            for _instance in instances:
                registry.update(_instance)
