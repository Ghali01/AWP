# Generated by Django 4.0.3 on 2022-03-07 13:06

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('articals', '0008_artical_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artical',
            name='img',
            field=models.FileField(default='', upload_to=pathlib.PureWindowsPath('C:/Users/zakaa/Desktop/project/mysite/photo')),
        ),
    ]
