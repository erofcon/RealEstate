from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.apartments_list, name='apartments_list'),
    path('<int:pk>/', views.single_apartment, name='single_apartment'),
    path('<str:category_id>/', views.apartments_list, name='category'),

]
