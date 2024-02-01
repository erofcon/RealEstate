from django.urls import path

from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.how_sale, name='how_sale'),
    path('post', views.sale, name='post'),
]
