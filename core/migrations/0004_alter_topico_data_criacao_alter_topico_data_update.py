# Generated by Django 4.2.9 on 2024-01-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_topico_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='data_criacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Criado'),
        ),
        migrations.AlterField(
            model_name='topico',
            name='data_update',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado'),
        ),
    ]