# Generated by Django 5.0.2 on 2024-07-11 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_application_installcmd'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sripts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('script', models.TextField()),
            ],
        ),
    ]
