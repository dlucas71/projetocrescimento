from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.contato, name='contato'),
    path('', views.sobre, name='sobre'),
]

# from django.conf.urls import patterns, include, url
#
# urlpatterns = patterns('courses.views',
#     url(r'^$', 'index', name='index'),
# )