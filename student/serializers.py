from rest_framework import serializers

from section.models import Section
from student.models import Student, StudentToSection


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'age', 'specialization']


class StudentToSectionSerializer(serializers.ModelSerializer):
    section = serializers.PrimaryKeyRelatedField(queryset=Section.objects.all(), write_only=True)

    class Meta:
        model = StudentToSection
        fields = ['student', 'section', 'date']