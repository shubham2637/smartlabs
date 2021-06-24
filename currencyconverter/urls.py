
from django.urls import path

from currencyconverter import views

urlpatterns = [
    path('',views.index,name='index'),
]