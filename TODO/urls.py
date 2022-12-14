"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from authors.views import AuthorModelViewSet, AuthorCustomViewSet, AuthorListAPIView
from memoapp.views import ProjectModelViewSet, TodoModelViewSet, ProjectDjangoFilterViewSet, TodoDjangoFilterViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="todo",
        default_version='v1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@mail.ru"),
        license=openapi.License(name="MIT License"),
        ),
    public=True,
    #permission_classes=(AllowAny,),
)


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
router.register('project', ProjectModelViewSet)
router.register('todo', TodoModelViewSet)
router.register('authors_custom', AuthorCustomViewSet)
router.register('project_filter', ProjectDjangoFilterViewSet)
router.register('todo_filter', TodoDjangoFilterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/<str:version>/authors/', AuthorListAPIView.as_view()),
    #path('swagger<str:format>/', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    ]

