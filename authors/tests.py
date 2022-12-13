import json
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
#from mixer.backend.django import mixer
from django.contrib.auth.models import User
from .views import AuthorModelViewSet
from .models import Author

class TestAuthorViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/authors/')
        view = AuthorModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'username': 'Пушкин', 'firstname': 'Александр', 'lastname': 'Пушкин',
                                                 'email': 'pushkin1799@bk.ru'}, format='json')
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        factory = APIRequestFactory()
        request = factory.post('/api/authors/', {'username': 'Пушкин', 'firstname': 'Александр', 'lastname': 'Пушкин',
                                                 'email': 'pushkin1799@bk.ru'}, format='json')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        force_authenticate(request, admin)
        view = AuthorModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail(self):
        author = Author.objects.create(username='Пушкин', firstname='Александр', lastname='Пушкин', email='pushkin1799@bk.ru')
        client = APIClient()
        response = client.get(f'/api/authors/{author.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_guest(self):
        author = Author.objects.create(username='Пушкин', firstname='Александр', lastname='Пушкин', email='pushkin1799@bk.ru')
        client = APIClient()
        response = client.put(f'/api/authors/{author.id}/', {'username': 'Пушкин', 'firstname': 'Александр', 'lastname': 'Пушкин',
                                                             'email': 'pushkin@bk.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_edit_admin(self):
        author = Author.objects.create(username='Пушкин', firstname='Александр', lastname='Пушкин', email='pushkin1799@bk.ru')
        client = APIClient()
        admin = User.objects.create_superuser('admin', 'admin@admin.com',
                                              'admin123456')
        client.login(username='admin', password='admin123456')
        response = client.put(f'/api/authors/{author.id}/', {'username': 'Лавкрафт', 'firstname': 'Говард', 'lastname': 'Лавкрафт',
                                                             'email': 'cthulhu@bk.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        author = Author.objects.get(id=author.id)
        self.assertEqual(author.firstname, 'Говард')
        self.assertEqual(author.email, 'cthulhu@bk.ru')
        client.logout()

class TestMath(APISimpleTestCase):
    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)



