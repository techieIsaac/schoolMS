# Generated by Django 2.1.7 on 2019-08-19 09:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_auto_20190819_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpresence',
            name='Attendance_Date',
            field=models.DateField(default=datetime.datetime(2019, 8, 19, 9, 37, 33, 324045, tzinfo=utc)),
        ),
    ]
