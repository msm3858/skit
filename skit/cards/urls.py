from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

app_name = 'cards'

urlpatterns = [
    # ex: /
    path('', login_required(views.IndexView.as_view()), name='index'),

    # Card views

    # ex: /card-list/all/
    path('card-list/all/', login_required(views.CardListView.as_view()), name='card_list'),
    # ex: /card-list/taken
    path('card-list/taken/', login_required(views.TakenCardListView.as_view()), name='taken_card_list'),
    # ex: /card-list/free
    path('card-list/free', login_required(views.FreeCardListView.as_view()), name='free_card_list'),
    # ex: /card/1/
    path('card/<int:pk>/', login_required(views.CardDetailView.as_view()), name='card_detail'),
    # ex: /card/add/
    path('card/add/', login_required(views.CardCreateView.as_view()), name='card_add'),
    # ex: /card/1/edit
    path('card/<int:pk>/edit/', login_required(views.CardUpdateView.as_view()), name='card_update'),
    # ex: /card/1/delete
    path('card/<int:pk>/delete/', login_required(views.CardDeleteView.as_view()), name='card_delete'),

    # EmployeeCardUsage views

    # ex: /employee_card_usage-list/
    path('employee_card_usage-list/', login_required(views.EmployeeCardUsageListView.as_view()),
         name='employee_card_usage_list'),
    # ex: /employee_card_usage/2/
    path('employee_card_usage/<int:pk>/', login_required(views.EmployeeCardUsageDetailView.as_view()),
         name='employee_card_usage_detail'),
    # ex: /employee_card_usage/add/
    path('employee_card_usage/add/', login_required(views.EmployeeCardUsageCreateView.as_view()),
         name='employee_card_usage_add'),
    # ex: /employee_card_usage/2/edit
    path('employee_card_usage/<int:pk>/edit/', login_required(views.EmployeeCardUsageUpdateView.as_view()),
         name='employee_card_usage_update'),
    # ex: /employee_card_usage/2/delete
    path('employee_card_usage/<int:pk>/delete/', login_required(views.EmployeeCardUsageDeleteView.as_view()),
         name='employee_card_usage_delete'),

    # VisitorCardUsage views

    # ex: /visitor_card_usage-list/
    path('visitor_card_usage-list/', login_required(views.VisitorCardUsageListView.as_view()),
         name='visitor_card_usage_list'),
    # ex: /visitor_card_usage/2/
    path('visitor_card_usage/<int:pk>/', login_required(views.VisitorCardUsageDetailView.as_view()),
         name='visitor_card_usage_detail'),
    # ex: /visitor_card_usage/add/
    path('visitor_card_usage/add/', login_required(views.VisitorCardUsageCreateView.as_view()),
         name='visitor_card_usage_add'),
    # ex: /visitor_card_usage/2/edit
    path('visitor_card_usage/<int:pk>/edit/', login_required(views.VisitorCardUsageUpdateView.as_view()),
         name='visitor_card_usage_update'),
    # ex: /visitor_card_usage/2/delete
    path('visitor_card_usage/<int:pk>/delete/', login_required(views.VisitorCardUsageDeleteView.as_view()),
         name='visitor_card_usage_delete'),
]
