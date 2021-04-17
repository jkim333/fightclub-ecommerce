from django.shortcuts import render
from allauth.account.views import PasswordChangeView

class CustomPasswordChangeView(PasswordChangeView):
    success_url = '/'