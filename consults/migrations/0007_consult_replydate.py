# Generated by Django 4.0.3 on 2022-05-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consults', '0006_consult_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='replyDate',
            field=models.DateField(null=True),
        ),
    ]