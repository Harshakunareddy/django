# Generated by Django 4.1.5 on 2023-02-04 14:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StudentModel',
            new_name='Student',
        ),
    ]