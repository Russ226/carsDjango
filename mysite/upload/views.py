from django.shortcuts import render
from cars.models import CarsInfo
from django.utils.datastructures import MultiValueDictKeyError
from django.utils.datetime_safe import datetime
from django.contrib.auth.decorators import login_required



@login_required(login_url='/login/')
def upload_car(request):
    if request.method == 'GET':
        return render(request, 'upload/upload.html')

    if request.method == 'POST':
        try:
            form = CarsInfo(make=request.POST.get('make'),model=request.POST.get('model'),release_year=request.POST.get('release_year')
                            ,car_pic=request.POST.get('car_pic'),pub_date=datetime.now())
            form.save()
            return render(request, '/')
        except:
            pass
    else:
        form = CarsInfo()
    #cars = carsInfo.objects.all()
    return render(request, 'upload/upload.html')



