# Generated by Django 2.2.4 on 2023-06-17 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20230617_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
