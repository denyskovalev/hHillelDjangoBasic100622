# Generated by Django 4.0.5 on 2022-06-11 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('breed', models.CharField(max_length=100)),
                ('weight', models.FloatField(max_length=100)),
            ],
        ),
    ]
