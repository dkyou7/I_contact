

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:board_id>', views.detail , name = 'detail'),
    path('new', views.new, name = 'new'),
    path('create', views.create, name= 'create'),
    path('edit/<int:board_id>', views.edit, name ="edit"),
    path('update/<int:board_id>', views.update, name = "update"),
    path('delete/<int:board_id>', views.delete, name = "delete"),
    path('', views.home, name='home'),

]