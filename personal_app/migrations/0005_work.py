# Generated by Django 5.0.2 on 2024-05-08 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_app', '0004_home'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('python', models.CharField(max_length=50)),
                ('java', models.CharField(max_length=50)),
                ('c', models.CharField(max_length=30)),
                ('django', models.CharField(max_length=50)),
                ('Html', models.CharField(max_length=30)),
                ('css', models.CharField(max_length=30)),
            ],
        ),
    ]
