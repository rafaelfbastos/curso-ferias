# Generated by Django 4.2.9 on 2024-01-23 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome'),
        ),
    ]