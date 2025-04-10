# Generated by Django 5.2 on 2025-04-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('bio', models.TextField()),
                ('birth_date', models.DateField()),
                ('nationality', models.CharField(max_length=100)),
            ],
        ),
    ]
