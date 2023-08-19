# Generated by Django 3.0.8 on 2023-02-03 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20230112_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 597491)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 597401)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 597465)),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 597519)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='otp_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 596370)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='profile_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 596276)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='signup_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 596348)),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='unique_code_time',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 3, 22, 13, 48, 596410)),
        ),
    ]
