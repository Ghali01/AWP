# Generated by Django 4.0.3 on 2022-04-28 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consults', '0003_alter_consult_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='consult',
            name='age',
            field=models.PositiveIntegerField(default=21),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consult',
            name='email',
            field=models.EmailField(default='g@t.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consult',
            name='gender',
            field=models.CharField(default='F', max_length=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consult',
            name='history',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consult',
            name='name',
            field=models.CharField(default='name', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='consult',
            name='phone',
            field=models.CharField(default='0', max_length=10),
            preserve_default=False,
        ),
    ]
