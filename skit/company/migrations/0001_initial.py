# Generated by Django 2.0.5 on 2019-02-05 17:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('department', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ('department', 'position', 'last_name', 'name'),
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('number_of_participants', models.PositiveIntegerField()),
                ('kind', models.CharField(choices=[('in', 'Wewnętrzne'), ('ext', 'Zewnętrzne'), ('con', 'Konferencja')], default='in', max_length=5)),
            ],
            options={
                'ordering': ['number_of_participants', 'description'],
            },
        ),
        migrations.CreateModel(
            name='MeetingParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employees', models.ManyToManyField(related_name='employees_meeting_participants', to='company.Employee')),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_meeting_participant_participant', to='company.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('capacity', models.PositiveIntegerField()),
                ('stuff', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomReservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(null=True)),
                ('meeting', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_meeting_reservation', to='company.Meeting')),
                ('reserved_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_employee_reservation', to='company.Employee')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_room_reservation', to='company.Room')),
            ],
            options={
                'ordering': ('-start_time', '-end_time', 'room'),
            },
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('purpose_of_visit', models.TextField()),
                ('status', models.CharField(choices=[('in', 'Inside'), ('out', 'Outside')], default='out', max_length=5)),
                ('description', models.TextField(null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees_visitor', to='company.Employee')),
            ],
            options={
                'ordering': ('employee', 'last_name', 'name', 'status'),
            },
        ),
        migrations.AddField(
            model_name='meetingparticipant',
            name='visitors',
            field=models.ManyToManyField(related_name='visitors_meeting_participants', to='company.Visitor'),
        ),
    ]
