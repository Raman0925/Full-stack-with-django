# Generated by Django 4.2.7 on 2023-12-07 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('first_name', models.IntegerField()),
                ('roll', models.IntegerField()),
            ],
        ),
    ]
