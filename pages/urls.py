from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('developments/', views.developments, name="developments"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name='dashboard'),
]