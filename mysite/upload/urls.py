from django.conf.urls import url,include
from django.views.generic import ListView

from . import views


urlpatterns = [url(r'^',views.upload_car,name='upload')]