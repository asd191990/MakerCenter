# Generated by Django 4.0.1 on 2022-03-14 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0013_course_typeshow_alter_news_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='typeshow',
        ),
    ]
