# Generated by Django 2.0.7 on 2018-07-23 08:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180719_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='container',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 23, 14, 1, 51, 437204)),
        ),
        migrations.AlterField(
            model_name='container',
            name='downvote',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='container',
            name='upvote',
            field=models.IntegerField(default=0),
        ),
    ]
