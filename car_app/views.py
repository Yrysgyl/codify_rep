from django.shortcuts import render, redirect
from .models import Category, Color, Car
from .forms import CarCreateForm
from .forms import CarForm
from django.db.models import Q


def index_view(request):
    cars = Car.objects.all()

    if 'search' in request.GET:
        search = request.GET['search']
        cars = Car.objects.filter(Q(title__icontains=search) | Q(description__icontains=search))

    return render(request, 'car_app/index.html', {'cars': cars})

def car_create_view(request):
    categories = Category.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        model = request.POST['model']
        year = request.POST['year']
        odometer = request.POST['odometer']
        engine_capacity = request.POST['engine_capacity']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(title=title, category=category, model=model, year=year, odometer=odometer,
                  engine_capacity=engine_capacity, color=color, image=image)
        car.save()

        return redirect('home')

    return render(request, 'car_app/car_create.html', context={"categories": categories, "colors": colors})


def car_create_view_2(request):

    if request.method == 'POST':
        form = CarCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("index")

    form = CarCreateForm()

    return render(request, template_name='car_app/car_create_2.html', context={'form': form})


def car_detail_view(request, pk):
    car = Car.objects.get(id=pk)

    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES, instance=car)
        if form.is_valid():
            form.save()
            return redirect("detail", car.id)

    form = CarForm(instance=car)

    return render(request, 'car_app/car_detail.html', {'car': car, 'form': form})


def car_detail_view_2(request, pk):
    categories = Category.objects.all()
    colors = Color.objects.all()
    car = Car.objects.get(id=pk)

    if request.method == 'POST':
        title = request.POST['title']
        model = request.POST['model']
        year = request.POST['year']
        odometer = request.POST['odometer']
        engine_capacity = request.POST['engine_capacity']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car.title = title
        car.model = model
        car.year = year
        car.odometer = odometer
        car.engine_capacity = engine_capacity
        car.color_id = color
        car.category_id = category
        car.image = image
        car.save()
        return redirect('index')

    return render(request=request, template_name='car_app/car_detail_2.html', context={'car': car, 'categories': categories,
                                                                                 'colors': colors})


def car_delete_view(request, pk):
    car = Car.objects.get(id=pk)
    car.delete()

    return redirect('index')