# Generated by Django 4.0.3 on 2022-04-08 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consults', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='reply',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]