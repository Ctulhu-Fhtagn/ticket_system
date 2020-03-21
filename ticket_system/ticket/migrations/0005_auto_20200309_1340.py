# Generated by Django 3.0.3 on 2020-03-09 13:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticket', '0004_auto_20200222_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Department'),
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(choices=[('n', 'Normal'), ('l', 'Low'), ('h', 'High')], default='h', help_text='For chosing priority your task', max_length=1),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('2d', 'To do'), ('iw', 'Inwork'), ('rv', 'Review'), ('dn', 'Done'), ('pp', 'Postponed')], default='2d', max_length=10),
        ),
    ]
