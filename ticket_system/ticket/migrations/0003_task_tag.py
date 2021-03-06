# Generated by Django 3.0.3 on 2020-03-29 09:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('ticket', '0002_auto_20200329_0943'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='tag',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
