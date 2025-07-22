from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .models import Car, Category
from .forms import CarCreateForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def main_page(request):
    cars=Car.objects.all()
    if request.user.is_authenticated:
        permit=True
    else:
        permit=False
    return render(request, 'app/main_page.html', {'cars': cars, 'permit': permit})


def detail_page(request,car_id):
    car=Car.objects.filter(id=car_id).first()
    return render(request, 'app/detail_page.html', {'car': car})

def add_model(request):
    categories=Category.objects.all()
    if request.method == "POST":
        owner=request.user
        name=request.POST['name']
        category_id=request.POST['category_id']
        category=Category.objects.get(id=category_id)
        year=request.POST['year']
        price=request.POST['price']
        model=request.POST['model']
        condition=request.POST['condition']
        car=Car(owner=owner,name=name,category=category,year=year,price=price,model=model,condition=condition,image = request.FILES['image'])
        car.save()
        return redirect('main_page')

    return render(request, 'app/create_page.html',{'categories': categories})

def update_car(request,car_id):
    car=Car.objects.get(id=car_id)
    categories=Category.objects.all()
    if request.method == "POST":
        car.name=request.POST['name']
        category_id=request.POST['category_id']
        car.category=Category.objects.get(id=category_id)
        car.year=request.POST['year']
        car.price=request.POST['price']
        car.model=request.POST['model']
        car.condition=request.POST['condition']
        car.image=request.FILES['image']
        car.save()
        return redirect('main_page')
    return render(request, 'app/update_car.html',{'car': car, 'categories': categories})


def create_car_2(request):
    if request.method == 'POST':
        form = CarCreateForm(request.POST,request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('main_page')
    else:
        form = CarCreateForm()

    return render(request, 'app/create_page_2.html', {'form': form})
        

def delete_car(request,car_id):
        car=Car.objects.get(id=car_id)
        car.delete()
        return redirect('main_page')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created, you can now login')
            return redirect('main_page')

        for field , errors in form.errors.items():
            for error in errors:
                messages.error(request, error)

    form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request=request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему')
            return redirect('main_page')

        messages.error(request, 'Неправильный логин или пароль')

    return render(request, 'app/Login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('main_page')