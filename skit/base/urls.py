from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth.decorators import login_required

app_name = 'base'

urlpatterns = [
    # ex: /
    path('', login_required(views.IndexView.as_view()), name='index'),
]
