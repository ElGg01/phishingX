# Generated by Django 5.1 on 2024-08-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('x', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='password',
            field=models.CharField(default='', max_length=64),
        ),
    ]
