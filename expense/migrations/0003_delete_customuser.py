# Generated by Django 5.0 on 2024-01-25 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0002_customuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
