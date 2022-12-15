from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from .models import Author
from .serializers import AuthorModelSerializer, AuthorModelCustomSerializer, AuthorFullModelSerializer


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

class AuthorCustomViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin, GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelCustomSerializer

class AuthorListAPIView(ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == 'v2':
            return AuthorFullModelSerializer
        return AuthorModelSerializer






