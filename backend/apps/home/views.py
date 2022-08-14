import os

from django.shortcuts import render
from django.views.generic.base import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        print(os.getcwd())
        return render(request, 'home/index.html')
