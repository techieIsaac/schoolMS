# Generated by Django 2.1.7 on 2019-08-19 09:22

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20190819_1221'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPresence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_Attendance', models.CharField(choices=[('1', 'Present'), ('0', 'Absent')], default='none', max_length=8, null=True)),
                ('Attendance_Date', models.DateField(default=datetime.datetime(2019, 8, 19, 9, 22, 55, 32740, tzinfo=utc))),
                ('Student_Name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.DataStudent')),
            ],
        ),
        migrations.RemoveField(
            model_name='studentattendance',
            name='Student_Name',
        ),
        migrations.DeleteModel(
            name='StudentAttendance',
        ),
    ]
