from django.urls import path
from . import views


urlpatterns = [
    path('', views.car_list, name='base'),
    path('<slug:car_slug>/', views.car_detail, name='car_detail'),
]