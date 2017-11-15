from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import Context
from django.template import RequestContext
from django.template import loader

from cars.models import CarsInfo


def search(request):
    return render(request,'search/fields.html')

def results(request):
    model = request.GET.get('model')
    make = request.GET.get('make')
    release_year =request.GET.get('release_year')

    result = CarsInfo.objects.filter()

    if model:
        result = result.filter(model__icontains = model)
    if make:
        result = result.filter(make__icontains = make)
    if release_year:
        result = result.filter(release_year__icontains = release_year)
    if not( model or make or release_year):
         return render(request, 'search/fields.html')

    context= {'object_list': result}

    return render(request,'search/results.html',context)
