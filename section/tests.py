from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from section.models import Section
from user.models import User


class SectionCreateTest(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', role='admin', password='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_section(self):
        url = reverse('sections-list')
        data = {'name': 'box', 'cost': '1000'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Section.objects.count(), 1)
        self.assertEqual(Section.objects.get().name, 'box')

    def test_create_section_role_not_admin(self):
        user = User.objects.create_user(username='user', role='user', password='user')
        self.client.force_authenticate(user=user)
        url = reverse('sections-list')
        data = {'name': 'box', 'cost': '1000'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class SectionTest(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', role='admin', password='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.section = Section.objects.create(name='box', cost=1000)

    def test_get_all_section(self):
        url = reverse('sections-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'box')
        self.assertEqual(response.data['results'][0]['cost'], 1000)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_section(self):
        url = reverse('sections-detail', kwargs={'pk': self.section.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'box')
        self.assertEqual(response.data['cost'], 1000)

    def test_update_section(self):
        url = reverse('sections-detail', kwargs={'pk': self.section.id})
        data = {'name': 'box_test', 'cost': '500'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Section.objects.count(), 1)
        self.assertEqual(Section.objects.get().name, 'box_test')
        self.assertEqual(Section.objects.get().cost, 500)

    def test_delete_section(self):
        url = reverse('sections-detail', kwargs={'pk': self.section.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Section.objects.count(), 0)


