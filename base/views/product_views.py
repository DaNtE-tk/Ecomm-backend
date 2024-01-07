from math import prod
from django.shortcuts import render
# from django.http import JsonResponse
# from base.products import products
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from base.serializer import ProductSerializer
# from django.contrib.auth.models import User

from base.models import Product

# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
# from django.contrib.auth.hashers import make_password
from rest_framework import status


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def getProducts(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def getUsers(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)


@api_view(['GET']) 
def getProduct(request,pk):
    product = Product.objects.get(_id=pk)
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user
    data = request.data
    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample brand',
        countInStock=0,
        category='sample category',
        description=''
    )
    # for i in products:
    #     if i['_id'] == pk:
    #         product = i
    #         break
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request,pk):
    data = request.data
    product = Product.objects.get(_id=pk)
    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()
   
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request,pk):
    productForDeletion = Product.objects.get(_id=pk)
    productForDeletion.delete()
    return Response('Product was deleted')


@api_view(['POST'])
@permission_classes([IsAdminUser])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)
    product.image = request.FILES.get('image')
    product.save()
    
    return Response('Image was uploaded')