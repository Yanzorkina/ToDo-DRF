from django.urls import path, include

from authors.views import AuthorListAPIView


app_name = 'authors'

urlpatterns = [
    path('', AuthorListAPIView.as_view())
]