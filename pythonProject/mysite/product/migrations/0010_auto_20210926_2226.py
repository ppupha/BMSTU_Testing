# Generated by Django 2.2 on 2021-09-26 19:26

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210926_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='createTime',
            field=models.DateTimeField(verbose_name=datetime.datetime(2021, 9, 26, 22, 26, 31, 509675)),
        ),
    ]
