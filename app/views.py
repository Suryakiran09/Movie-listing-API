from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend

class PaginationClass(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 100
    
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = PaginationClass
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'year', 'rating', 'actors__name', 'genres__name', 'technicians__name']