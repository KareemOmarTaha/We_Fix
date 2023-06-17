# Generated by Django 2.2.4 on 2023-06-17 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20230617_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='users_who_dislike',
            field=models.ManyToManyField(related_name='disliked_freelancer', to='login_app.User'),
        ),
        migrations.AlterField(
            model_name='freelancer',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_freelancer', to='login_app.User'),
        ),
    ]
