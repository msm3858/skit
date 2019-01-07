from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
import uuid


# Create your models here.
class Human(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    active = models.BooleanField(default=True)

    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} {} active: {}".format(self.name, self.last_name, self.active)

    def get_absolute_url(self):
        return reverse('company:human_detail',
                       args=[self.uuid])

    class Meta:
        abstract = True
        ordering = ('-level_of_privilege', 'status', 'last_name', 'name')


class Employee(Human):
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    class Meta:
        ordering = ('department', 'position', 'last_name', 'name')


class Visitor(Human):
    STATUS_CHOICES = (
        ('in', 'Inside'),
        ('out', 'Outside'),
    )

    purpose_of_visit = models.TextField(null=False)
    employee = models.ForeignKey(Employee,
                                 on_delete=models.SET_NULL,
                                 related_name='employees_visitor',
                                 null=True)
    status = models.CharField(max_length=5,
                              choices=STATUS_CHOICES,
                              default='out')
    description = models.TextField(null=True)

    class Meta:
        ordering = ('employee', 'last_name', 'name', 'status')


class Room(models.Model):
    name = models.CharField(max_length=50,
                            null=False,
                            unique=True)
    capacity = models.PositiveIntegerField()
    stuff = models.TextField()

    def __str__(self):
        return "Name: {}, capacity: {}.".format(self.name, self.capacity)


class CardUsage(models.Model):
    description = models.TextField(null=False, unique=False)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)

    # TODO: Received from
    # TODO: Given to

    def __str__(self):
        return "[{}] Taken: {}, given back: {}".format(self.description, self.start_time, self.end_time)

    class Meta:
        abstract = True
        ordering = ('-startTime', '-endTime', 'description')


class Meeting(models.Model):
    KIND_CHOICES = (
        ('in', 'Internal'),
        ('ext', 'External'),
        ('con', 'Conference'),
    )
    description = models.TextField()
    number_of_participants = models.PositiveIntegerField()
    kind = models.CharField(max_length=5,
                            choices=KIND_CHOICES,
                            default='in')

    def __str__(self):
        return "{}, number of participants: {}.".format(self.description[:20], self.number_of_participants)

    class Meta:
        ordering = ['number_of_participants', 'description']


class MeetingParticipant(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    meeting = models.ForeignKey(Meeting,
                                on_delete=models.SET_NULL,
                                related_name='company_meeting_participant_participant',
                                null=True)
    visitors = models.ManyToManyField(Visitor,
                                      related_name='visitors_meeting_participants')
    employees = models.ManyToManyField(Employee,
                                       related_name='employees_meeting_participants')

    # created = models.DateTimeField(auto_now_add=True, null=False)
    # updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return "[Uuid: {}, meeting: {}]".format(self.id, self.meeting.description[:20])


class RoomReservation(models.Model):
    room = models.ForeignKey(Room,
                             on_delete=models.SET_NULL,
                             related_name='company_room_reservation',
                             null=True)
    meeting = models.ForeignKey(Meeting,
                                on_delete=models.SET_NULL,
                                related_name='company_meeting_reservation',
                                null=True)
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=True)
    reserved_by = models.ForeignKey(Employee,
                                    on_delete=models.SET_NULL,
                                    related_name='company_employee_reservation',
                                    null=True)

    def __str__(self):
        return "Room: {} reserved by: {}, at {} to {}.".format(
            self.room.name, self.reserved_by, self.start_time, self.end_time)

    class Meta:
        ordering = ('-start_time', '-end_time', 'room')
