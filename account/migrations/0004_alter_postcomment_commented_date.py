# Generated by Django 4.0.4 on 2022-09-21 10:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_postcomment_commented_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='commented_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 9, 21, 16, 29, 28, 377267)),
        ),
    ]