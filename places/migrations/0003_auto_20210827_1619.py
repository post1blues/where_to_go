# Generated by Django 3.2.6 on 2021-08-27 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='order',
            new_name='serial_number',
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
