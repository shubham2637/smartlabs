from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item,Order

@api_view(['POST'])
def listorder(request):
    try:
        user_id = request.POST['user_id']
        user = User.objects.get(id=user_id)
    except Exception as e:
        Response(str(e),status=status.HTTP_404_NOT_FOUND)
    userDetails = {
        "username" : user.username,
        "email" : user.email
    }
    items = Item.objects.filter(order__user=user)
    context = {
        "user" : userDetails,
        "items": items.values('name','price','quantity','total'),
        #"subtotal" : items.
    }
