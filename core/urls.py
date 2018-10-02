from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.contato, name='contato'),
    path('', views.sobre, name='sobre'),
]