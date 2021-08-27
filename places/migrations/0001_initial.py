# Generated by Django 3.2.6 on 2021-08-27 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_short', models.CharField(max_length=500)),
                ('description_long', models.TextField()),
                ('lng', models.FloatField()),
                ('lat', models.FloatField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]