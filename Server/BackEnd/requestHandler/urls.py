from django.urls import path
from requestHandler import views

urlpatterns = [
    path('index/', views.index),
    path('images/', views.images),
    path('country_status/', views.country_status),
    path('list_country/', views.list_country),
    path('check/', views.check),

]
