# Generated by Django 3.2.6 on 2021-09-08 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_auto_20210829_0049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'ordering': ['-date_created'], 'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.RenameField(
            model_name='place',
            old_name='created_date',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
