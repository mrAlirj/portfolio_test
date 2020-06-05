from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

class home(TemplateView):

    def get(self , request , **kwargs):
        jobs = job.objects.all()

        context = {
            'jobs': jobs
        }
        return render(request , 'jobs/home.html' , context)
