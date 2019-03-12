import uuid
import os

from django.db import models
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils.deconstruct import deconstructible


@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filePath):
        name, ext = filePath.split('.')[:-1], filePath.split('.')[-1]
        if instance.id:
            filePath = '{}.{}'.format(instance.id, ext)
        else:
            filePath = '{}.{}'.format(uuid.uuid4().hex, ext)

        instance.name = name[0]
        instance.extension = ext
        # return the whole path to the file
        return os.path.join(self.sub_path, filePath)


class BaseDocument(models.Model):
    DOCUMENT_KINDS = (
        ('pdf', 'PDF'),
        ('wrd', 'Word'),
        ('xls', 'Excel'),
        ('pst', 'Prezentacja'),
        ('oth', 'Inne'),
    )
    kind_of_document = models.CharField(max_length=3,
                                        choices=DOCUMENT_KINDS,
                                        default='pdf')

    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=False, blank=True, )
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    updated = models.DateTimeField(auto_now=True, null=True)

    file = models.FileField(upload_to=UploadToPathAndRename(os.path.join('documents/')))
    extension = models.CharField(
        max_length=10,
        null=False,
        db_index=True,
        validators=[RegexValidator(regex='^(\S{1,10})$',
                                   message='Inappropriate file extension. Must be numeric.',
                                   code='invalid_file_extension'
                                   )
                    ],
        blank=True,
    )

    class Meta:
        abstract = True
        ordering = ('-created', 'name')


class MeetingDocument(BaseDocument):
    meeting = models.ForeignKey('company.Meeting',
                                on_delete=models.CASCADE,
                                related_name='meeting_documents')
    file = models.FileField(upload_to=UploadToPathAndRename(os.path.join('MeetingDocuments/')))

    def __str__(self):
        return "{}.{} - {}".format(self.id, self.extension, self.name)

    def get_absolute_url(self):
        return reverse('document:meeting_document_detail',
                       args=[self.id])

    class Meta:
        ordering = ('name', 'extension')


class EmployeeDocument(BaseDocument):
    employee = models.ForeignKey('company.Employee',
                                 on_delete=models.CASCADE,
                                 related_name='employee_documents')
    file = models.FileField(upload_to=UploadToPathAndRename(os.path.join('EmployeeDocuments/')))

    def __str__(self):
        return "{}.{} - {}".format(self.id, self.extension, self.name)

    class Meta:
        ordering = ('name', 'extension')

    def get_absolute_url(self):
        return reverse('document:employee_document_detail',
                       args=[self.id])
