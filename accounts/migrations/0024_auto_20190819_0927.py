# Generated by Django 2.1.7 on 2019-08-19 06:27

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_auto_20190816_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Attendance', models.CharField(choices=[('1', 'Present'), ('0', 'Absent')], default='none', max_length=8, null=True)),
                ('Attendance_Date', models.DateField(default=datetime.datetime(2019, 8, 19, 6, 27, 3, 31043, tzinfo=utc))),
            ],
        ),
        migrations.RemoveField(
            model_name='datastudent',
            name='Student_Attendance',
        ),
        migrations.RemoveField(
            model_name='datastudent',
            name='created_at',
        ),
        migrations.AddField(
            model_name='studentattendance',
            name='Student_Name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.DataStudent'),
        ),
    ]
