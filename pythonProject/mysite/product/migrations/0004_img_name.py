# Generated by Django 2.2 on 2021-09-25 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210925_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='img',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
