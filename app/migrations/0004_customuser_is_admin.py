# Generated by Django 3.0.5 on 2023-09-06 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]
