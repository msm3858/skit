from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

app_name = 'company'

urlpatterns = [
    # ex: /
    path('', login_required(views.IndexView.as_view()), name='index'),

    # Employee views

    # ex: /employee-list/
    path('employee-list/', login_required(views.EmployeeListView.as_view()), name='employee_list'),
    # ex: /employee/fc9591ea-2865-11e9-b210-d663bd873d93/
    path('employee/<uuid:pk>/', login_required(views.EmployeeDetailView.as_view()), name='employee_detail'),
    # ex: /employee/add/
    path('employee/add/', login_required(views.EmployeeCreateView.as_view()), name='employee_add'),
    # ex: /employee/fc9591ea-2865-11e9-b210-d663bd873d93/edit
    path('employee/<uuid:pk>/edit/', login_required(views.EmployeeUpdateView.as_view()), name='employee_update'),
    # ex: /employee/fc9591ea-2865-11e9-b210-d663bd873d93/delete
    path('employee/<uuid:pk>/delete/', login_required(views.EmployeeDeleteView.as_view()), name='employee_delete'),

    # Visitor views

    # ex: /visitor-list/
    path('visitor-list/', login_required(views.VisitorListView.as_view()), name='visitor_list'),
    # ex: /visitor/fc9591ea-2865-11e9-b210-d663bd873d93/
    path('visitor/<uuid:pk>/', login_required(views.VisitorDetailView.as_view()), name='visitor_detail'),
    # ex: /visitor/add/
    path('visitor/add/', login_required(views.VisitorCreateView.as_view()), name='visitor_add'),
    # ex: /visitor/fc9591ea-2865-11e9-b210-d663bd873d93/edit
    path('visitor/<uuid:pk>/edit/', login_required(views.VisitorUpdateView.as_view()), name='visitor_update'),
    # ex: /visitor/fc9591ea-2865-11e9-b210-d663bd873d93/delete
    path('visitor/<uuid:pk>/delete/', login_required(views.VisitorDeleteView.as_view()), name='visitor_delete'),

    # Room views

    # ex: /room-list/
    path('room-list/', login_required(views.RoomListView.as_view()), name='room_list'),
    # ex: /room/33/
    path('room/<int:pk>/', login_required(views.RoomDetailView.as_view()), name='room_detail'),
    # ex: /room/add/
    path('room/add/', login_required(views.RoomCreateView.as_view()), name='room_add'),
    # ex: /room/5/edit
    path('room/<int:pk>/edit/', login_required(views.RoomUpdateView.as_view()), name='room_update'),
    # ex: /room/5/delete
    path('room/<int:pk>/delete/', login_required(views.RoomDeleteView.as_view()), name='room_delete'),

    # Meeting views

    # ex: /meeting-list/
    path('meeting-list/', login_required(views.MeetingListView.as_view()), name='meeting_list'),
    # ex: /meeting/21/
    path('meeting/<int:pk>/', login_required(views.MeetingDetailView.as_view()), name='meeting_detail'),
    # ex: /meeting/add/
    path('meeting/add/', login_required(views.MeetingCreateView.as_view()), name='meeting_add'),
    # ex: /meeting/21/edit
    path('meeting/<int:pk>/edit/', login_required(views.MeetingUpdateView.as_view()), name='meeting_update'),
    # ex: /meeting/21/delete
    path('meeting/<int:pk>/delete/', login_required(views.MeetingDeleteView.as_view()), name='meeting_delete'),
    # ex: /meeting/21/add-participants/
    path('meeting/<int:meeting_id>/add-participants/',
         login_required(views.FromMeetingAddMeetingParticipantCreateView.as_view()), name='meeting_add_participants'),

    # MeetingParticipant views

    # ex: /meeting_participant-list/
    path('meeting_participant-list/', login_required(views.MeetingParticipantListView.as_view()),
         name='meeting_participant_list'),
    # ex: /meeting_participant/fc9591ea-2865-11e9-b210-d663bd873d93/
    path('meeting_participant/<uuid:pk>/', login_required(views.MeetingParticipantDetailView.as_view()),
         name='meeting_participant_detail'),
    # ex: /meeting_participant/add/
    path('meeting_participant/add/', login_required(views.MeetingParticipantCreateView.as_view()),
         name='meeting_participant_add'),
    # ex: /meeting_participant/fc9591ea-2865-11e9-b210-d663bd873d93/edit
    path('meeting_participant/<uuid:pk>/edit/', login_required(views.MeetingParticipantUpdateView.as_view()),
         name='meeting_participant_update'),
    # ex: /meeting_participant/fc9591ea-2865-11e9-b210-d663bd873d93/delete
    path('meeting_participant/<uuid:pk>/delete/', login_required(views.MeetingParticipantDeleteView.as_view()),
         name='meeting_participant_delete'),

    # RoomReservation views

    # ex: /room_reservation-list/
    path('room_reservation-list/', login_required(views.RoomReservationListView.as_view()),
         name='room_reservation_list'),
    # ex: /room_reservation/12/
    path('room_reservation/<int:pk>/', login_required(views.RoomReservationDetailView.as_view()),
         name='room_reservation_detail'),
    # ex: /room_reservation/add/
    path('room_reservation/add/', login_required(views.RoomReservationCreateView.as_view()),
         name='room_reservation_add'),
    # ex: /room_reservation/12/edit
    path('room_reservation/<int:pk>/edit/', login_required(views.RoomReservationUpdateView.as_view()),
         name='room_reservation_update'),
    # ex: /room_reservation/12/delete
    path('room_reservation/<int:pk>/delete/', login_required(views.RoomReservationDeleteView.as_view()),
         name='room_reservation_delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
