
from django.urls import path

from currencyconverter import views

urlpatterns = [
    path('listorder',views.index,name='Index api'),
]