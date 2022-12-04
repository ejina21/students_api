import datetime

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse

from section.models import Section
from student.models import Student, StudentToSection
from user.models import User


class StudentCreateTest(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', role='admin', password='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)

    def test_create_student(self):
        url = reverse('students-list')
        data = {'name': 'artem', 'age': '20', 'specialization': 'worker'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'artem')
        self.assertEqual(Student.objects.get().age, 20)

    def test_create_student_role_not_admin(self):
        user = User.objects.create_user(username='user', role='user', password='user')
        self.client.force_authenticate(user=user)
        url = reverse('students-list')
        data = {'name': 'artem', 'age': '20', 'specialization': 'worker'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class StudentTest(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', role='admin', password='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.student = Student.objects.create(name='artem', age=20, specialization='worker')

    def test_get_all_students(self):
        url = reverse('students-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'artem')
        self.assertEqual(response.data['results'][0]['age'], 20)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_student(self):
        url = reverse('students-detail', kwargs={'pk': self.student.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'artem')
        self.assertEqual(response.data['age'], 20)

    def test_update_student(self):
        url = reverse('students-detail', kwargs={'pk': self.student.id})
        data = {'name': 'Andry', 'age': '25'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Student.objects.count(), 1)
        self.assertEqual(Student.objects.get().name, 'Andry')
        self.assertEqual(Student.objects.get().age, 25)

    def test_delete_student(self):
        url = reverse('students-detail', kwargs={'pk': self.student.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Student.objects.count(), 0)


class StudentToSectionTest(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create_superuser(username='admin', role='admin', password='admin')
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.student = Student.objects.create(name='artem', age=20, specialization='worker')
        self.section = Section.objects.create(name='box', cost=100)

    def test_create_instance(self):
        url = reverse('add_to_section')
        data = {'student': self.student.id, 'section': self.section.id, 'date': datetime.date(2000, 1, 1)}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(StudentToSection.objects.count(), 1)
        self.assertEqual(StudentToSection.objects.get().student, self.student)
        self.assertEqual(StudentToSection.objects.get().section, self.section)
        self.assertEqual(StudentToSection.objects.get().date, datetime.date(2000, 1, 1))

    def test_create_instance_role_not_admin(self):
        user = User.objects.create_superuser(username='user', role='user', password='admin')
        self.client.force_authenticate(user=user)
        url = reverse('add_to_section')
        data = {'student': self.student.id, 'section': self.section.id, 'date': datetime.date(2000, 1, 1)}
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



