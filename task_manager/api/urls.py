from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, TaskDocumentViewSet


router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'search', TaskDocumentViewSet, basename='search')


urlpatterns = [
    path('', include(router.urls)),
]
