from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from rest_framework import serializers

from .documents import TaskDocument
from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Task.
    """
    class Meta:
        model = Task
        fields = '__all__'


class TaskDocumentSerializer(DocumentSerializer):
    """
    Сериализатор для документа Elasticsearch TaskDocument.
    """
    class Meta:
        document = TaskDocument

    field = ('title',
             'description')
