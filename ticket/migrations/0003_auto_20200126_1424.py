# Generated by Django 3.0.1 on 2020-01-26 11:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20200126_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ticket.Department'),
        ),
    ]