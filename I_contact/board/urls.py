

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('board', views.board , name = 'board'),
    path('<int:board_id>', views.detail , name = 'detail'),
    path('new', views.new, name = 'new'),
    path('create', views.create, name= 'create'),
    path('edit/<int:board_id>', views.edit, name ="edit"),
    path('update/<int:board_id>', views.update, name = "update"),
    path('delete/<int:board_id>', views.delete, name = "delete"),
    path('new_comment/<int:detail_id>', views.new_comment, name = "new_comment"),


]