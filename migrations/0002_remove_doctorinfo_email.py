# Generated by Django 3.1.3 on 2020-12-28 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctorinfo',
            name='Email',
        ),
    ]
