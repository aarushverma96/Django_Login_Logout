# log/urls.py
from django.conf.urls import url    #importing url lib
from . import views					#importing views from current dir

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
]