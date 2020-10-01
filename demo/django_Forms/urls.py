from django.urls import path
from django.conf.urls import url
from . import views
# from .views import CustomLogin
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.create_View),
   path('edit/<id>/', views.edit),
   path('update/', views.update_View),
   path('delete/<id>/', views.delete_View),

   
]