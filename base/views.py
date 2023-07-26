from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductSerializer 

from .models import Product
# Create your views here.

@api_view(['GET'])
def getRoute(request):
    return Response('Hello')

@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
 
@api_view(['GET']) 
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)
