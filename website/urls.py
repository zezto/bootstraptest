from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('bamboozled/', views.details, name="bamboozled"),
    path('bamboozled/about', views.about, name="about"),
    path('bamboozled/terms', views.terms, name="terms"),
    

]
