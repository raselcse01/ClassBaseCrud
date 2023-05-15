from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView


# Create your views here.
class ProfileTemplateView(TemplateView):
    template_name = 'registration/profile.html'

