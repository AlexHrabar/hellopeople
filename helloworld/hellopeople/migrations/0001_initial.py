# Generated by Django 4.0.1 on 2022-01-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35, verbose_name="Ім'я")),
                ('surname', models.CharField(max_length=35, verbose_name='Прізвище')),
            ],
        ),
    ]
