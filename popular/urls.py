from django.urls import path

from . import views

urlpatterns = [
    path('api/v1/products/popular', views.index, name='index'),
]