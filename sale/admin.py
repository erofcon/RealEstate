from django.contrib import admin

from .models import ExternalApartments
from catalog.models import Images


class ImagesAdmin(admin.StackedInline):
    model = Images


@admin.register(ExternalApartments)
class ApartmentsAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]
    list_display = ('title', 'status', 'external', 'show', 'date')

    list_filter = (
        ('show', admin.BooleanFieldListFilter),
        'status',
        'show',
        'external',
    )

    class Meta:
        model = ExternalApartments


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
