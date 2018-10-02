from django.contrib import admin
from django.urls import include, path
from core import views
#from courses import views

urlpatterns = [
    path('', views.home, name='home'),
    path('core/contato/', views.contato, name='contato'),
    path('core/sobre/', views.sobre, name='sobre'),
    #path('courses/index/', views.courses, name='index'),

    path('admin/', admin.site.urls),
]