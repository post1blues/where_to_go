# Generated by Django 3.2.6 on 2021-09-08 13:44

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_auto_20210908_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(default='long description', verbose_name='Полное описание'),
            preserve_default=False,
        ),
    ]
