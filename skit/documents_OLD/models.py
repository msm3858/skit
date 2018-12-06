import uuid
import os

from django.apps import apps
from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone
from django.utils.deconstruct import deconstructible


class BaseDocument(models.Model):

    STATUS_CHOICES = (
        ('s', 'Sent'),
        ('p', 'Pending'),
        ('e', 'Error'),
        ('l', 'Loaded'),
    )

    DOCUMENT_KINDS = (
        ('pdf', 'PDF'),
        ('wrd', 'Word'),
        ('xls', 'Excel'),
        ('pst', 'Presentation'),
        ('oth', 'Other'),
    )
    kind_of_document = models.CharField(max_length=3,
                                        choices=DOCUMENT_KINDS,
                                        default='pdf')

    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default='l')

    extension = models.CharField(
                            max_length=10,
                            null=False,
                            db_index=True,
                            validators=[RegexValidator(regex='^(\S{1,10})$'
                                                       , message='Inappropriate file extension. Must be numeric.',
                                                       code='invalid_file_extension')
                                        ]
                            )
    file = models.FileField()

    class Meta:
        abstract = True
        ordering = ('-created', 'name')


class ConferenceDocument(BaseDocument):
    employee = models.ForeignKey(apps.get_model('company', 'Employee'),
                                 on_delete=models.SET_NULL,
                                 related_name='employee_documents',
                                 null=True)
    conference = models.ForeignKey(apps.get_model('company', 'Conference'),
                                   on_delete=models.SET_NULL,
                                   related_name='conference_documents')
    file = models.FileField(upload_to='conferenceDocuments/%Y/%m/%d')

    def __str__(self):
        return "{}.{} - {}".format(self.uuid, self.extension, self.name)




    class Meta:
       ordering = ('conference', 'kind_of_document', 'name')

# class EmployeeDocument(BaseDocument):
#     employee = models.ForeignKey(apps.get_model('company', 'Employee'),
#                                  on_delete=models.SET_NULL,
#                                  related_name='employee_documents',
#                                  null=True)
#     file = models.FileField(upload_to='employeeDocuments/%Y/%m/%d')
#
#     def __str__(self):
#         return "{}.{} - {}".format(self.uuid, self.extension, self.name)
#
#     class Meta:
#         ordering = ('-created', 'kind_of_document', 'name')
#
#
#
#
#
