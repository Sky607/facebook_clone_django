# Generated by Django 4.0.6 on 2022-10-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='Group_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to='Group/images'),
        ),
    ]
