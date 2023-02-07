from django.urls import path

from . import views
# from .views import ResturantApiView

urlpatterns = [
    path('', views.getRoutes, name='getRoute'),
    
    path('api/v1/users/', views.getUsers, name='getUsers'),
    path('api/v1/user/<str:username>/', views.getUser, name='getUser'),
    
    path('api/v1/profiles/', views.getProfiles, name='getProfiles'),
    path('api/v1/profile/<str:username>/', views.getProfile, name='getProfile'),

    path('api/v1/resturants/', views.getResturants, name='getResturants'),
    path('api/v1/resturant/add/', views.addResturant, name='addResturant'),
    path('api/v1/resturant/<str:pk>/', views.getResturant, name='getResturant'),
    path('api/v1/resturant/edit/<str:pk>/', views.editResturant, name='editResturant'),
    path('api/v1/resturant/delete/<str:pk>/', views.deleteResturant, name='deleteResturant'),

    # path('api/v1/resturant/<str:username>/', ResturantApiView.as_view()),
]