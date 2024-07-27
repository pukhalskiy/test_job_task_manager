from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry

from tasks.models import Task


@registry.register_document
class TaskDocument(Document):
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
        #settings = {'number_of_shards': 1, 'number_of_replicas': 0}

    class Django:
        model = Task
        #fields = [
        #    'title',
        #    'description'
        #]
