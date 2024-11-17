# Generated by Django 5.0.7 on 2024-11-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.CharField(max_length=150, verbose_name='Марка')),
                ('model', models.CharField(max_length=150, verbose_name='Модель')),
                ('country', models.CharField(max_length=100, verbose_name='Країна')),
                ('power', models.IntegerField(verbose_name='Потужність')),
                ('fuel', models.CharField(choices=[('gasoline', 'Бензин'), ('diesel', 'Дизель'), ('propane', 'Пропан'), ('electricity', 'Електрика'), ('hybrid', 'Гібрид')], default='gasoline', max_length=15, verbose_name='Тип палива')),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('exists', 'Є в наявності'), ('not exists', 'Немає в наявності')], default='exists', max_length=15, verbose_name='Статус')),
                ('slug', models.SlugField(max_length=150, unique='mark')),
            ],
            options={
                'verbose_name': 'Авто',
                'verbose_name_plural': 'Автомобілі',
                'ordering': ('mark', 'model'),
            },
        ),
    ]
