from django.urls import path
from appname import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.user_login, name='login'),
    path('exit', views.log_out, name='exit')
]
