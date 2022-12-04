from rest_framework.viewsets import ModelViewSet
from student.models import Student, StudentToSection
from rest_framework import filters
from student.permissions import CustomPermission
from student.serializers import StudentSerializer, StudentToSectionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [CustomPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['age']
    search_fields = ['name']
    ordering_fields = ['name', 'age']


class AddStudentToSectionAPIView(CreateAPIView):
    queryset = StudentToSection.objects.all()
    serializer_class = StudentToSectionSerializer
    permission_classes = [CustomPermission]
