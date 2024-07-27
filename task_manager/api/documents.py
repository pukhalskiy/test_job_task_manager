from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from tasks.models import Task


@registry.register_document
class TaskDocument(Document):
    """
    Представление документа Elasticsearch для модели Task.
    """
    title = fields.TextField(
        attr='title',
        fields={
            'raw': fields.TextField()
        }
    )
    description = fields.TextField(
        attr='description',
        fields={
            'raw': fields.TextField()
        }
    )

    class Index:
        name = 'tasks'

    class Django:
        model = Task
