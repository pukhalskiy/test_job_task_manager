from rest_framework.pagination import PageNumberPagination

from core.constants import PAGE_LENGTH


class ApiPagination(PageNumberPagination):
    """
    Пагинация для API.
    """
    page_size_query_param = "limit"
    page_size = PAGE_LENGTH
