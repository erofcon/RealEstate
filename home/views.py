from django.shortcuts import render

from catalog.models import Apartments


def index(request):
    last_apartments = Apartments.objects.filter(show=True).order_by('-date')[:6]

    data = {'apartments': last_apartments}

    return render(request, 'home.html', context=data)
