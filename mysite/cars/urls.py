from django.conf.urls import url,include
from . import views
from django.views.generic import ListView, DetailView
from .models import CarsInfo

# urlpatterns = [url(r'^', ListView.as_view(queryset=CarsInfo.objects.all().order_by("-pub_date"),
#                 template_name="cars/posts.html"))]

urlpatterns  = [url(r'^$',views.index,name='index')]