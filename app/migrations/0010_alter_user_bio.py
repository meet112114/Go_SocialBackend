# Generated by Django 5.0.3 on 2024-03-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_userfollow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.CharField(default='Update your bio', max_length=164, null=True),
        ),
    ]
