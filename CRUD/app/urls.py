from django.contrib import admin
from django.urls import path

from app import views


urlpatterns = [
    
    path('', views.UserAddShowView.as_view(), name='addandshow'),
    path('delete/<int:id>', views.UserDelete.as_view(), name='deletedata'),
    path('update/<int:id>', views.UserUpdateView.as_view(), name='uudatedata'),
    

       # path('', add_show, name='add_show') 
       # path('delete/<int:id>/', delete, name='delete'),
       # path('<int:id>/', update, name="update"),
   

]