# Generated by Django 3.2.6 on 2021-08-27 22:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20210828_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='my_field',
        ),
        migrations.AlterField(
            model_name='place',
            name='description_long',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
