from typing import Any
from django.shortcuts import render
from django.views.generic import *
# Create your views here.


class HealthCareHomeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, *args,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='narendra'
        context['ram']='ram'
        context['gopal']='hari'
        return context