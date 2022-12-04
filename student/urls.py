from django.urls import path

from student.views import AddStudentToSectionAPIView

urlpatterns = [
    path('v1/add_to_section/', AddStudentToSectionAPIView.as_view(), name='add_to_section'),
]