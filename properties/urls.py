from django.urls import path
from properties import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.properties, name="properties"),
    path('<int:pk>/', views._property, name="property"),
    path('search/', views.search, name="search"),
] 

