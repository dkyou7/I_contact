from django.urls import path

from . import views

urlpatterns = [
<<<<<<< HEAD
    # path('', views.index, name='index'),
=======
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name= 'login'),
    path('logout/',views.logout, name= 'logout'),
>>>>>>> 82657cdf38bdc6347256fe7fba9b32b2094f15d0
]