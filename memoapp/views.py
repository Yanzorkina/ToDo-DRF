from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import Project, Todo
from .serializers import ProjectModelSerializer, TodoModelSerializer
from .filter import ProjectFilter, TodoFilter


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    pagination_class = ProjectLimitOffsetPagination

class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination

class ProjectDjangoFilterViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer
    filterset_class = ProjectFilter
    pagination_class = ProjectLimitOffsetPagination

class TodoDjangoFilterViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    filterset_class = TodoFilter
    pagination_class = TodoLimitOffsetPagination
