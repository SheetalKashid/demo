# Generated by Django 2.0.7 on 2018-07-09 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='joining_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='employee',
            name='salary',
            field=models.IntegerField(null=True),
        ),
    ]
