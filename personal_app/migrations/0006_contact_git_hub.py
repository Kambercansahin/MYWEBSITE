# Generated by Django 5.0.2 on 2024-05-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_app', '0005_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='git_hub',
            field=models.CharField(default='', max_length=150),
        ),
    ]
