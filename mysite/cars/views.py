from django.shortcuts import render
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from .models import CarsInfo


def index(request):
    car_list = CarsInfo.objects.all().order_by("-pub_date")
    paginator = Paginator(car_list,20)
    page =request.GET.get('page')

    try:
        objects_list = paginator.page(page)
    except PageNotAnInteger:
        objects_list = paginator.page(1)
    except EmptyPage:
        objects_list = paginator.page(paginator.num_pages)

    return render(request,'cars/posts.html',{'objects_list':objects_list})

# def post(request):
#     return render(request,'cars/posts.html')