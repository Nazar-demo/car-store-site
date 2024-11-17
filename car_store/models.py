from django.db import models
from django.urls import reverse


class Car(models.Model):
    FUEL_CHOICES = (
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('propane', 'Пропан'),
        ('electricity', 'Електрика'),
        ('hybrid', 'Гібрид'),
    )

    STATUS_CHOICES = (
        ('exists', 'Є в наявності'),
        ('not exists', 'Немає в наявності'),
    )

    mark = models.CharField(max_length=150, verbose_name='Марка')
    model = models.CharField(max_length=150, verbose_name='Модель')
    country = models.CharField(max_length=100, verbose_name='Країна')
    power = models.IntegerField(verbose_name='Потужність')
    fuel = models.CharField(max_length=15, choices=FUEL_CHOICES, default='gasoline', verbose_name='Тип палива')
    description = models.TextField(blank=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='exists', verbose_name='Статус')
    slug = models.SlugField(max_length=150, unique='mark')

    class Meta:
        ordering = ('mark', 'model')
        verbose_name = 'Авто'
        verbose_name_plural = 'Автомобілів'

    def __str__(self):
        return f'{self.mark} {self.model}'

    def get_absolute_url(self):
        return reverse('car_store:car_detail', args=(self.slug,))