# Generated by Django 4.0.6 on 2022-10-13 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_group_group_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='Group_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='Group/images'),
        ),
    ]
