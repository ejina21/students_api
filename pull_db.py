import datetime
import random
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_student.settings')
django.setup()

from user.models import User
from student.models import Student, StudentToSection
from section.models import Section

User.objects.create_superuser(username='admin', password='admin', role='admin')
User.objects.create_user(username='user', password='user', role='user')

to_create_students = []
to_create_sections = []
to_create_m2m = []

for i in range(30):
    to_create_students.append(Student(
        name=f'Test_{i}',
        age=20,
        specialization='worker',
    ))
    to_create_sections.append(Section(
        name=f'Test section {i}',
        cost=random.randint(100, 5000),
    ))
Student.objects.bulk_create(to_create_students)
Section.objects.bulk_create(to_create_sections)

student1 = Student.objects.get(id=1)
student2 = Student.objects.get(id=2)

for section in Section.objects.all()[:5]:
    to_create_m2m.append(StudentToSection(
        student=student1,
        section=section,
        date=datetime.date.today(),
    ))
    to_create_m2m.append(StudentToSection(
        student=student2,
        section=section,
        date=datetime.date.today(),
    ))
StudentToSection.objects.bulk_create(to_create_m2m)