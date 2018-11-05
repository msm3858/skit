# Generated by Django 2.0.5 on 2018-11-05 20:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_meeting_kind'),
        ('cards', '0004_auto_20181105_2027'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeCardUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.Card')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards_employee_card_usage', to='company.Employee')),
            ],
            options={
                'ordering': ('employee', '-start_time', '-end_time', 'description'),
            },
        ),
        migrations.CreateModel(
            name='VisitorCardUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('card', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cards.Card')),
                ('visitor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cards_visitor_card_usage', to='company.Visitor')),
            ],
            options={
                'ordering': ('visitor', '-start_time', '-end_time', 'description'),
            },
        ),
    ]
