# Generated by Django 4.2.7 on 2023-12-01 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.IntegerField()),
                ('flight_name', models.CharField(max_length=30)),
                ('flight_time', models.FloatField()),
            ],
        ),
    ]
