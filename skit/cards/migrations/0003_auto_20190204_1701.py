# Generated by Django 2.0.5 on 2019-02-04 17:01

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20190204_1655'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='card',
            options={'ordering': ('level_of_privilege', 'name', 'status')},
        ),
        migrations.AlterModelManagers(
            name='card',
            managers=[
                ('taken', django.db.models.manager.Manager()),
            ],
        ),
    ]