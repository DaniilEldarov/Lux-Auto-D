from django.shortcuts import render
from .models import Car
# Create your views here.
def main_page(request):
    cars=Car.objects.all()
    return render(request, 'app/main_page.html', {'cars': cars})


def detail_page(request,car_id):
    car=Car.objects.filter(id=car_id).first()
    return render(request, 'app/detail_page.html', {'car': car})