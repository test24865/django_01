# Generated by Django 3.2 on 2021-04-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20210414_1023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=250, verbose_name='Краткое описание'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Заголовок'),
        ),
    ]