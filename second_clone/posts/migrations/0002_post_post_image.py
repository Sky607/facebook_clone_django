# Generated by Django 4.0.6 on 2022-09-30 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='post/images'),
        ),
    ]
