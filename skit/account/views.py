from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': dashboard})