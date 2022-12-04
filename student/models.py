from django.db import models

from section.models import Section


class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя студента')
    age = models.SmallIntegerField(null=True, blank=True, verbose_name='Возраст студента')
    specialization = models.CharField(max_length=100, blank=True, null=True, verbose_name='Наименование специальности')
    sections = models.ManyToManyField(
        Section,
        verbose_name='Посещаемые секции',
        related_name='student',
        through='StudentToSection',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class StudentToSection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, verbose_name='Секция', related_name='m2m')
    date = models.DateField(verbose_name='Дата зачисления на секцию')

    def __str__(self):
        return f'{self.student} - {self.section}'

    class Meta:
        unique_together = ('student', 'section')
        verbose_name = 'Связь студента с секцией'
        verbose_name_plural = 'Связи студентов с секциями'
