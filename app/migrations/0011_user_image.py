# Generated by Django 5.0.3 on 2024-03-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_alter_user_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, default='media/profile_images/defaultprp.jpg', null=True, upload_to='profile_images/'),
        ),
    ]
