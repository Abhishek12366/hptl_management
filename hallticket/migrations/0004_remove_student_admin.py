# Generated by Django 3.0.5 on 2023-09-07 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hallticket', '0003_student_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='admin',
        ),
    ]
