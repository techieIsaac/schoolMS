# Generated by Django 2.1.7 on 2019-08-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20190816_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastudent',
            name='Student_Attendance',
            field=models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='none', max_length=130, null=True),
        ),
    ]
