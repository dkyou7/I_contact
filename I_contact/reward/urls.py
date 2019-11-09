from django.urls import path

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('reward/',views.reward, name='reward'),
    path('new', views.new, name = 'new_reward'),
    path('create', views.create, name= 'create_reward'),
    path('<int:reward_id>', views.detail , name = 'detail_reward'),

]