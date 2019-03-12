from django.db import models
from django.urls import reverse
import uuid
from django.core.exceptions import ValidationError


class Human(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=50, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return "{} {} active: {}".format(self.name, self.last_name, self.active)

    def get_absolute_url(self):
        return reverse('company:human_detail',
                       args=[self.id])

    class Meta:
        abstract = True
        ordering = ('last_name', 'name', 'active')


class Employee(Human):
    department = models.CharField(max_length=255)
    position = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('company:employee_detail',
                       args=[self.id])

    class Meta:
        ordering = ('department', 'position', 'last_name', 'name')


class Visitor(Human):
    STATUS_CHOICES = (
        ('in', 'Wewnątrz'),
        ('out', 'Na zewnątrz'),
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

    def get_absolute_url(self):
        return reverse('company:visitor_detail',
                       args=[self.id])

    class Meta:
        ordering = ('employee', 'last_name', 'name', 'status')


class Room(models.Model):
    name = models.CharField(max_length=50,
                            null=False,
                            unique=True)
    capacity = models.PositiveIntegerField()
    stuff = models.TextField()

    def get_absolute_url(self):
        return reverse('company:room_detail',
                       args=[self.id])

    def __str__(self):
        return "Name: {}, capacity: {}.".format(self.name, self.capacity)


class Meeting(models.Model):
    KIND_CHOICES = (
        ('in', 'Wewnętrzne'),
        ('ext', 'Zewnętrzne'),
        ('con', 'Konferencja'),
    )
    description = models.TextField()
    number_of_participants = models.PositiveIntegerField()
    kind = models.CharField(max_length=5,
                            choices=KIND_CHOICES,
                            default='in')

    def __str__(self):
        return "{}, number of participants: {}.".format(self.description[:20], self.number_of_participants)

    def get_absolute_url(self):
        return reverse('company:meeting_detail',
                       args=[self.id])

    class Meta:
        ordering = ['number_of_participants', 'description']


class MeetingParticipant(models.Model):
    meeting = models.ForeignKey(Meeting,
                                on_delete=models.SET_NULL,
                                related_name='company_meeting_participant_participant',
                                null=True,
                                unique=True,
                                )
    visitors = models.ManyToManyField(Visitor,
                                      related_name='visitors_meeting_participants')
    employees = models.ManyToManyField(Employee,
                                       related_name='employees_meeting_participants')

    # created = models.DateTimeField(auto_now_add=True, null=False)
    # updated = models.DateTimeField(auto_now=True, null=True)
    def get_absolute_url(self):
        return reverse('company:meeting_participant_detail',
                       args=[self.id])

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
    end_time = models.DateTimeField(null=True, blank=True)
    reserved_by = models.ForeignKey(Employee,
                                    on_delete=models.SET_NULL,
                                    related_name='company_employee_reservation',
                                    null=True)

    def get_absolute_url(self):
        return reverse('company:room_reservation_detail',
                       args=[self.id])

    def __str__(self):
        return "Room: {} reserved by: {}, at {} to {}.".format(
            self.room.name, self.reserved_by, self.start_time, self.end_time)

    def clean(self):
        cleaned_start_time = self.start_time
        cleaned_end_time = self.end_time
        cleaned_room = self.room
        # Where cleaned_start_time is between start_time and end_time
        reserved_conflicts = RoomReservation.objects.filter(room=cleaned_room.id)
        reserved_conflicts_inner1 = reserved_conflicts.filter(start_time__lte=cleaned_start_time)
        reserved_conflicts_inner1 = reserved_conflicts_inner1.filter(end_time__gte=cleaned_start_time)
        if reserved_conflicts_inner1.count() > 0:
            raise ValidationError(("SALA JUŻ ZAREZERWOWANA."))

        # Where cleaned_end_time is between start_time and end_time
        reserved_conflicts_inner2 = reserved_conflicts.filter(start_time__lte=cleaned_end_time)
        reserved_conflicts_inner2 = reserved_conflicts_inner2.filter(end_time__gte=cleaned_end_time)
        if reserved_conflicts_inner2.count() > 0:
            raise ValidationError(("SALA JUŻ ZAREZERWOWANA."))
        # Where cleaned_start_time is pre start_time and cleaned_end_time is after end_time
        reserved_conflicts_outer = reserved_conflicts.filter(start_time__gte=cleaned_start_time)
        reserved_conflicts_outer = reserved_conflicts_outer.filter(end_time__lte=cleaned_end_time)
        if reserved_conflicts_outer.count() > 0:
            raise ValidationError(("SALA JUŻ ZAREZERWOWANA."))

    class Meta:
        ordering = ('-start_time', '-end_time', 'room')
