# Generated by Django 4.0.4 on 2022-09-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_postcomment_commented_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postcomment',
            name='commented_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
