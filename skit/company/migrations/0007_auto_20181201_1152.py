# Generated by Django 2.0.5 on 2018-12-01 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20181117_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='created',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='meetingparticipant',
            name='created',
        ),
        migrations.RemoveField(
            model_name='meetingparticipant',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='created',
        ),
        migrations.RemoveField(
            model_name='visitor',
            name='updated',
        ),
    ]
