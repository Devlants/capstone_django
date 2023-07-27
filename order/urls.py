from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.OrderCreateView),
    path('temperature/list',views.temperatureList)
]
