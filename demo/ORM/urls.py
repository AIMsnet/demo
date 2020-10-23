from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.oneToMany),
    path('showDiscovries/<id>/', views.showDiscovries),
    path('manyToMany/', views.manyToMany),
    path('showBook/<id>/', views.showBook),
    path('showAuthors/<id>/', views.showAuthors),

]