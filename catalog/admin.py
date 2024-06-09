from django.contrib import admin
from catalog.models import Images, Apartments


class ImagesAdmin(admin.StackedInline):
    model = Images


@admin.register(Apartments)
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
        model = Apartments


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass
