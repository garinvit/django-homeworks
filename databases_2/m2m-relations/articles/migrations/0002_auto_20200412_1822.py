# Generated by Django 2.2.10 on 2020-04-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationship',
            options={'verbose_name': 'Тема', 'verbose_name_plural': 'Тематики статьи'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Раздел', 'verbose_name_plural': 'Разделы'},
        ),
    ]
