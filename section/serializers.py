from rest_framework import serializers

from section.models import Section
from student.serializers import StudentToSectionSerializer


class SectionSerializer(serializers.ModelSerializer):
    students = StudentToSectionSerializer(source='m2m', many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'name', 'cost', 'students']
