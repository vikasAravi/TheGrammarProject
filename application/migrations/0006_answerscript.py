# Generated by Django 2.0.7 on 2018-07-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20180723_1425'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerScript',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField()),
            ],
        ),
    ]
