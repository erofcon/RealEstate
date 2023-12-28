from django.contrib import admin

from .models import Apartments, Images


class ImagesAdmin(admin.StackedInline):
    model = Images


@admin.register(Apartments)
class ApartmentsAdmin(admin.ModelAdmin):
    inlines = [ImagesAdmin]

    class Meta:
        model = Apartments


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
