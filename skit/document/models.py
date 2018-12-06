import uuid
import os

from django.apps import apps
from django.db import models

from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone
from django.utils.deconstruct import deconstructible


# def path_and_rename(path):
#     def wrapper(instance, filePath):
#         fileName, ext = filePath.split('.')[:-1], filePath.split('.')[-1]
#         if instance.uuid:
#             fileFieldPath = '{}.{}'.format(instance.uuid, ext)
#         else:
#             fileFieldPath = '{}.{}'.format(uuid.uuid4().hex, ext)
#         instance.name = fileName
#         instance.extension = ext
#         return os.path.join(path, fileFieldPath)
#     return wrapper

@deconstructible
class UploadToPathAndRename(object):

    def __init__(self, path):
        self.sub_path = path

    def __call__(self, instance, filePath):
        name, ext = filePath.split('.')[:-1], filePath.split('.')[-1]
        if instance.uuid:
            filePath = '{}.{}'.format(instance.uuid, ext)
        else:
            filePath = '{}.{}'.format(uuid.uuid4().hex, ext)

        instance.name = name
        instance.extension = ext
        # return the whole path to the file
        return os.path.join(self.sub_path, filePath)





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
    name = models.CharField(max_length=50, unique=False, blank=True,)
    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default='l',)

    extension = models.CharField(
                            max_length=10,
                            null=False,
                            db_index=True,
                            validators=[RegexValidator(regex='^(\S{1,10})$',
                                                       message='Inappropriate file extension. Must be numeric.',
                                                       code='invalid_file_extension',
                                                       )
                                        ],
                            blank=True,
                            )

    class Meta:
        abstract = True
        ordering = ('-created', 'name')


class MeetingDocument(BaseDocument):
    # meeting = models.ForeignKey(apps.get_model('company', 'Meeting'),
    #                             on_delete=models.SET_NULL,
    #                             related_name='meeting_documents')
    file = models.FileField(upload_to=UploadToPathAndRename(os.path.join('upload', 'here')))

    def __str__(self):
        return "{}.{} - {}".format(self.uuid, self.extension, self.name)

    class Meta:
        ordering = ('name', 'extension')

