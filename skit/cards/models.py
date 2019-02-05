from django.apps import apps
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify


class FreeCardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='free')


class TakenCardManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='taken')


# Create your models here.
class Card(models.Model):
    STATUS_CHOICES = (
        ('free', 'Wolna'),
        ('taken', 'Zajęta'),
    )
    PRIVILEGES_CHOICES = (
        ('employee', 'Pracownik'),
        ('guest', 'Gość'),
        ('master', 'Master'),
        ('stuff', 'Obsługa'),
    )
    name = models.CharField(max_length=50, unique=True)
    code = models.CharField(unique=True,
                            max_length=20,
                            null=False,
                            db_index=True,
                            validators=[RegexValidator(regex='^[0-9]+$',
                                                       message='Niepoprawny format karty. \
                                                        Kod karty może składać się tylko z cyfr 0-9.',
                                                       code='invalid_card_code'),
                                        ]
                            )
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='free')

    level_of_privilege = models.CharField(max_length=10,
                                          choices=PRIVILEGES_CHOICES,
                                          default='guest')
    objects = models.Manager()  # Common manager.
    free = FreeCardManager()  # Custom manager.
    taken = TakenCardManager()  # Custom manager.

    def __str__(self):
        return "{} {}".format(self.name, self.level_of_privilege)

    def get_absolute_url(self):
        return reverse('cards:card_detail',
                       args=[self.id])

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
        return "[{}] Taken by: {} at: {}, given back: {}.".format(self.employee, self.description, self.start_time,
                                                                  self.end_time)

    class Meta:
        ordering = ('employee', '-start_time', '-end_time', 'description')


class VisitorCardUsage(CardUsage):
    visitor = models.ForeignKey('company.Visitor',
                                on_delete=models.SET_NULL,
                                related_name='cards_visitor_card_usage',
                                null=True)

    def __str__(self):
        return "[{}] Taken by: {} at: {}, given back: {}.".format(self.visitor, self.description, self.start_time,
                                                                  self.end_time)

    class Meta:
        ordering = ('visitor', '-start_time', '-end_time', 'description')
