# Generated by Django 2.0.5 on 2018-12-02 13:30

import django.core.validators
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingDocument',
            fields=[
                ('kind_of_document', models.CharField(choices=[('pdf', 'PDF'), ('wrd', 'Word'), ('xls', 'Excel'), ('pst', 'Presentation'), ('oth', 'Other')], default='pdf', max_length=3)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('status', models.CharField(choices=[('s', 'Sent'), ('p', 'Pending'), ('e', 'Error'), ('l', 'Loaded')], default='l', max_length=1)),
                ('extension', models.CharField(db_index=True, max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_file_extension', message='Inappropriate file extension. Must be numeric.', regex='^(\\S{1,10})$')])),
                ('file', models.FileField(upload_to='MeetingDocuments/%Y/%m/%d/')),
            ],
            options={
                'ordering': ('name', 'extension'),
            },
        ),
        migrations.DeleteModel(
            name='ConferenceDocument',
        ),
    ]
