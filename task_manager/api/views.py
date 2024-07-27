from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import SearchFilterBackend

from tasks.tasks import process_task
from tasks.models import Task
from .serializers import TaskSerializer
from .paginations import ApiPagination
from .documents import TaskDocument
from .serializers import TaskDocumentSerializer


class TaskDocumentViewSet(DocumentViewSet):
    """
    Вьюсет модели документа Elasticsearch.
    """
    document = TaskDocument
    serializer_class = TaskDocumentSerializer

    filter_backends = [
        SearchFilterBackend
    ]
    search_fields = ('title',
                     'description')


class TaskViewSet(viewsets.ModelViewSet):
    """
    Вьюсет модели Task.
    Методы:
        update: Частичное обновление существующего объекта Task. Проверяет
            данные на валидность и сохраняет обновленный объект.
        destroy: Удаление существующего объекта Task. После удаления возвращает
            статус HTTP 204 (Нет содержимого).
        all_tasks: Возвращает список всех задач. Использует метод GET и
            сериализует список задач в формат JSON.
        perform_create: Создает новый объект Task. После создания задачи
            вызывает задачу в фоне для обработки через Celery.
        complete: Обновляет статус задачи на 'completed'. Использует метод POST
            и принимает идентификатор задачи в качестве параметра.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    pagination_class = ApiPagination

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,
                                         data=request.data,
                                         partial=partial)
        serializer.is_valid()
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def all_tasks(self, request):
        tasks = Task.objects.all()
        serializer = self.get_serializer(tasks, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        task = serializer.save()
        process_task.delay(task.id)

    @action(detail=True, methods=['POST'])
    def complete(self, request, pk=None):
        task = self.get_object()
        task.status = 'completed'
        task.save()
        return Response({'status': 'Task marked as completed'})
