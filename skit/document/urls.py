from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

app_name = 'document'

urlpatterns = [
    # ex: /document/
    path('', login_required(views.EmployeeDocumentListView.as_view()), name='employee_document_list'),
    # ex: /document/add/
    path('employeeDocument/add/', login_required(views.EmployeeDocumentCreateView.as_view()),
         name='employee_document_add'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/edit
    path('employeeDocument/<uuid:pk>/edit/', login_required(views.EmployeeDocumentUpdateView.as_view()),
         name='employee_document_update'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/delete
    path('employeeDocument/<uuid:pk>/delete/', login_required(views.EmployeeDocumentDeleteView.as_view()),
         name='employee_document_delete'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/
    path('employeeDocument/<uuid:pk>/', login_required(views.EmployeeDocumentDetailView.as_view()),
         name='employee_document_detail'),
    # ex: /document/add/
    path('meetingDocument/add/', login_required(views.MeetingDocumentCreateView.as_view()),
         name='meeting_document_add'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/edit
    path('meetingDocument/<uuid:pk>/edit/', login_required(views.MeetingDocumentUpdateView.as_view()),
         name='meeting_document_update'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/delete
    path('meetingDocument/<uuid:pk>/delete/', login_required(views.MeetingDocumentDeleteView.as_view()),
         name='meeting_document_delete'),
    # ex: /document/b26950fe-21c4-11e9-ab14-d663bd873d93/
    path('meetingDocument/<uuid:pk>/', login_required(views.MeetingDocumentDetailView.as_view()),
         name='meeting_document_detail'),
    path('meetingDocument-list/', login_required(views.MeetingDocumentListView.as_view()),
         name='meeting_document_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
