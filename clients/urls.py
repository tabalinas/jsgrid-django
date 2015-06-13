from django.conf.urls import url
from . import views
from .views import Clients

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/?$', Clients.as_view()),
    url(r'^api/(?P<client_id>[0-9]+)/?$', Clients.as_view()),
]