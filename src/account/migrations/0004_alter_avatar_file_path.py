# Generated by Django 3.2 on 2021-07-14 10:54

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='file_path',
            field=models.FileField(upload_to=account.models.user_avatar_upload),
        ),
    ]
