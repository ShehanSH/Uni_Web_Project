# Generated by Django 3.2.19 on 2023-07-26 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ground_booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ground',
            name='ground_image',
            field=models.ImageField(blank=True, null=True, upload_to='ground_images/'),
        ),
    ]
