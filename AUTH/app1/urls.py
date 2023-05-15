from django.contrib import admin
from django.urls import path

from app1 import views


urlpatterns = [
    
       path('profile/', views.ProfileTemplateView.as_view(), name="profile"),

       # path('', add_show, name='add_show') 
       # path('delete/<int:id>/', delete, name='delete'),
       # path('<int:id>/', update, name="update"),
   

]