# Generated by Django 3.1.7 on 2021-03-20 20:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Evoting_app', '0002_auto_20210321_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='register_date',
            field=models.DateField(default=datetime.datetime(2021, 3, 21, 1, 33, 9, 724118)),
        ),
    ]