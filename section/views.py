from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from section.models import Section
from section.serializers import SectionSerializer
from student.permissions import CustomPermission


class SectionViewSet(ModelViewSet):
    queryset = Section.objects.all().prefetch_related('m2m')
    serializer_class = SectionSerializer
    permission_classes = [CustomPermission]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['cost', 'm2m__student']
    search_fields = ['name']
    ordering_fields = ['name', 'cost']