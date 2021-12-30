# Generated by Django 3.2.8 on 2021-12-27 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Название продукта')),
                ('text', models.TextField(max_length=135, unique=True, verbose_name='Описание продукта')),
                ('img', models.ImageField(upload_to='images/', verbose_name='Изображение продукта')),
                ('category', models.CharField(choices=[('Ножи', 'Ножи'), ('Оружие', 'Оружие'), ('Наклейки', 'Наклейки'), ('Аксессуары', 'Аксессуары'), ('Одежда', 'Одежда')], default='Одежда', max_length=50, verbose_name='Категория продукта')),
                ('link_product', models.CharField(max_length=100, verbose_name='Ссылка на продукт')),
                ('date', models.DateTimeField(verbose_name='дата')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
                'ordering': ['name'],
            },
        ),
    ]