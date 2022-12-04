from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=100, verbose_name='Наименование секции')
    cost = models.IntegerField(verbose_name='Ежемесячная стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Секция'
        verbose_name_plural = 'Секции'