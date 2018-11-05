from django.apps import apps
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone


class FreeManager(models.Manager):
    def get_queryset(self):
        return super(FreeManager, self).get_queryset()\
                        .filter(status='free')

class TakenManager(models.Manager):
    def get_queryset(self):
        return super(TakenManager, self).get_queryset()\
                        .filter(status='taken')



# Create your models here.
class Card(models.Model):
    STATUS_CHOICES = (
        ('free', 'Free'),
        ('taken', 'Taken'),
    )
    PRIVILEGES_CHOICES = (
        ('employee', 'Employee'),
        ('guest', 'Guest'),
        ('master', 'Master'),
        ('stuff', 'Stuff'),
    )
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    code = models.CharField(unique=True,
                            max_length=20,
                            null=False,
                            db_index=True,
                            validators=[RegexValidator(regex='^[0-9]+$'
                                                       , message='Unpropriate card code. Must be numeric.',
                                                       code='invalid_card_code')
                                        , ]
                            )
    # code = models.BigIntegerField(unique=True,
    #                               null=False,
    #                               db_index=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='free')

    level_of_privilege = models.CharField(max_length=10,
                                          choices=PRIVILEGES_CHOICES,
                                          default='guest')
    # employee = models.ForeignKey(apps.get_model('company', 'Employee'),
    #                              on_delete=models.SET_NULL,
    #                              related_name='cards_card',
    #                              null=True)
    # taken = TakenManager()  # Our custom manager.
    free = FreeManager()  # Our custom manager.

    def __str__(self):
        return "{} {}".format(self.name, self.level_of_privilege)

    def get_absolute_url(self):
        return reverse('cards:card_detail',
                       args=[self.slug])

    class Meta:
        ordering = ('level_of_privilege', 'name', 'status')


class CardUsage(models.Model):
    description = models.TextField(null=False, unique=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)
    card = models.ForeignKey(Card,
                             on_delete=models.SET_NULL,
                             null=True)

    # TODO: Received from
    # TODO: Given to

    def __str__(self):
        return "[{}] Taken: {}, given back: {}".format(self.description, self.start_time, self.end_time)

    class Meta:
        abstract = True
        ordering = ('-startTime', '-endTime', 'description')


class EmployeeCardUsage(CardUsage):
    employee = models.ForeignKey('company.Employee',
                                 on_delete=models.SET_NULL,
                                 related_name='cards_employee_card_usage',
                                 null=True)

    def __str__(self):
        return "[{}] Taken by: {} at: {}, given back: {}.".format(self.employee, self.description, self.start_time, self.end_time)

    class Meta:
        ordering = ('employee', '-start_time', '-end_time', 'description')


class VisitorCardUsage(CardUsage):
    visitor = models.ForeignKey('company.Visitor',
                                on_delete=models.SET_NULL,
                                related_name='cards_visitor_card_usage',
                                null=True)

    def __str__(self):
        return "[{}] Taken by: {} at: {}, given back: {}.".format(self.visitor, self.description, self.start_time, self.end_time)

    class Meta:
        ordering = ('visitor', '-start_time', '-end_time', 'description')

