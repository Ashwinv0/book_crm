# Generated by Django 4.2.7 on 2024-02-06 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0005_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('course', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=35)),
            ],
        ),
    ]
