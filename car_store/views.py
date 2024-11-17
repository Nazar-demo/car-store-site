from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Car


def car_list(request):
    cars = Car.objects.all()

    paginator = Paginator(cars, 5)
    page = request.GET.get('page')

    try:
        cars = paginator.page(page)
    except PageNotAnInteger:
        cars = paginator.page(1)
    except EmptyPage:
        cars = paginator.page(paginator.num_pages)

    context = {
        'cars': cars,
        'page': page,
    }

    return render(request, 'car_store/index.html', context)


def car_detail(request, car_slug):
    car = get_object_or_404(
        Car,
        status='exists',
        slug=car_slug
    )

    return render(request, 'car_store/detail.html', {'car': car})