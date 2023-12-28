from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Apartments


def apartments_list(request, category_id='all'):
    all_category = ['for_sale', 'sales']

    if category_id in all_category:
        all_apartments = Apartments.objects.filter(status=category_id, show=True).order_by('-date')
    else:
        all_apartments = Apartments.objects.filter(show=True).order_by('-date')

    paginator = Paginator(all_apartments, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    data = {
        'page_obj': page_obj,
        'category': category_id,
    }

    return render(request, 'apartments_list.html', context=data)


def single_apartment(request, pk=None):
    print("hello")
    apartment = Apartments.objects.get(id=pk, show=True)

    data = {
        'apartment': apartment,
    }

    return render(request, 'single_apartment.html', context=data)
