# Generated by Django 3.0.3 on 2020-02-22 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_auto_20200222_1003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='priority_client',
            new_name='priority',
        ),
        migrations.RemoveField(
            model_name='task',
            name='priority_executor',
        ),
    ]