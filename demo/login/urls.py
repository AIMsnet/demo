from django.urls import path
from django.conf.urls import url
from . import views
# from .views import CustomLogin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.userLogin.as_view(template_name='loginPage.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('welcomPage/', views.welcomePage),
    path('logout/', views.logout),

]