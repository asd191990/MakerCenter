# Generated by Django 4.0.1 on 2022-03-07 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BackEnd', '0011_alter_course_type_alter_space_equipment_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classroomintroducts',
            options={'verbose_name': '校級共用實驗室借用情形', 'verbose_name_plural': '校級共用實驗室借用情形'},
        ),
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '課程列表', 'verbose_name_plural': '課程列表'},
        ),
        migrations.AlterModelOptions(
            name='downloadfiles',
            options={'verbose_name': '相關辦法', 'verbose_name_plural': '相關辦法'},
        ),
        migrations.AlterModelOptions(
            name='equipment',
            options={'verbose_name': '設備介紹', 'verbose_name_plural': '設備介紹'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': '專業領域小組', 'verbose_name_plural': '專業領域小組'},
        ),
        migrations.AlterModelOptions(
            name='memebers',
            options={'verbose_name': '成員', 'verbose_name_plural': '成員'},
        ),
        migrations.AlterModelOptions(
            name='space',
            options={'verbose_name': '空間介紹', 'verbose_name_plural': '空間介紹'},
        ),
    ]