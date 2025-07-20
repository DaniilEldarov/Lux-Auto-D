from django.shortcuts import render,redirect
from .models import Car, Category


# Create your views here.
def main_page(request):
    cars=Car.objects.all()
    return render(request, 'app/main_page.html', {'cars': cars})


def detail_page(request,car_id):
    car=Car.objects.filter(id=car_id).first()
    return render(request, 'app/detail_page.html', {'car': car})

def add_model(request):
    categories=Category.objects.all()
    if request.method == "POST":
        name=request.POST['name']
        category_id=request.POST['category_id']
        category=Category.objects.get(id=category_id)
        year=request.POST['year']
        price=request.POST['price']
        model=request.POST['model']
        condition=request.POST['condition']
        car=Car(name=name,category=category,year=year,price=price,model=model,condition=condition,image = request.FILES['image'])
        car.save()
        return redirect('main_page')

    return render(request, 'app/create_page.html',{'categories': categories})
