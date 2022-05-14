from django.urls import path

from . import views
from .views import ResturantApiView

urlpatterns = [
    path('', views.getRoute, name='getRoute'),
    path('api/v1/users/', views.getUsers, name='getUsers'),
    path('api/v1/user/<str:username>/', views.getUser, name='getUser'),
    path('api/v1/profiles/', views.getProfiles, name='getProfiles'),
    path('api/v1/profile/<str:username>/', views.getProfile, name='getProfile'),
    path('api/v1/resturants/', views.getResturants, name='getResturants'),
    path('api/v1/resturant/<str:username>/', views.getResturant, name='getResturant'),
    # path('api/v1/resturant/<str:username>/', ResturantApiView.as_view()),
]