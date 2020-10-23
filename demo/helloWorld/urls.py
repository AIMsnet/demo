from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path("", views.home),
    path("helloWorld/", views.index),
    path("add/", views.add),
    path("sub/", views.sub),
    path("multiply/", views.multiply),
    path("div/", views.div)


]