from typing import Any, Dict
from django.shortcuts import render, redirect, HttpResponseRedirect

from .forms import StudentRegistration
# from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView, RedirectView
from django.views import View


# Create your views here. class base view 
class UserAddShowView(TemplateView):
    template_name = 'addandshow.html'
    context_objects_name = 'stud'
    def get_context_data(self,**kwargs):
        context =  super().get_context_data(**kwargs)
        fm = StudentRegistration()
        # stud = User.objects.all()
        context = {'fm':fm}
        return context
    
    
    def post(self, request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
        return HttpResponseRedirect('/')
    
class UserDelete(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        # print(kwargs['id'])
        del_id = (kwargs['id'])
        User.objects.get(pk=del_id).delete()

        return super().get_redirect_url(*args, **kwargs)
    
class UserUpdateView(View):
    def get(self, request, id):
        pi = User.objects.get(pk = id)
        fm = StudentRegistration(instance=pi)
        return render(request, 'update.html', {'form':fm})

    def post(self, request, id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')



# def add_show(request):
#     return render(request, 'base.html')

# def update(request):
#     return render(request, 'base.html')

# def delete(request):
#     return render(request, 'base.html')
