from django.shortcuts import render
from django.http import JsonResponse

from .forms import ExternalApartmentsFormModel, ExternalApartmentsImagesForm
from catalog.models import Images


def how_sale(request):
    return render(request, 'how_sale.html')


def sale(request):
    if request.method == 'POST':

        form = ExternalApartmentsFormModel(request.POST, request.FILES)
       
        if form.is_valid():
            instance = form.save(commit=True)

            for f in request.FILES.getlist('image'):
                external = Images(
                    apartment=instance,
                    image=f
                )
                external.save()

            return JsonResponse("Успешно отправлено", status=200, safe=False)
        else:
            return JsonResponse(form.errors, status=400, safe=False)

    else:
        sale_form = ExternalApartmentsFormModel()
        images_form = ExternalApartmentsImagesForm()
        return render(request, 'sale.html', {'form': sale_form, 'images_form': images_form})
