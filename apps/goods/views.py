from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from apps.users.models import User
from apps.users.views import UserAddressView


class IndexView(View):
    def get(self, request):
        print(UserAddressView.__mro__)
        return render(request, 'index.html')
