from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.views import Response

from . import models
from . import serializers


# class CategoryListCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Category.objects.all()
#     serializer_class = serializers.CategorySerializer
#
#
# class ProductListCreateAPIView(generics.ListCreateAPIView):
#     queryset = models.Product.objects.all()
#     serializer_class = serializers.ProductSerializer


@api_view(http_method_names=['GET', 'POST'])
def category_list_create_api_view(request):

    if request.method == "GET":
        categories = models.Category.objects.all()
        serializer = serializers.CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        received_data = request.data
        serializer = serializers.CategorySerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'POST'])
def product_list_create_api_view(request):

    if request.method == "GET":
        products = models.Product.objects.all()
        serializer = serializers.ProductSerializer(instance=products, many=True)
        return Response(serializer.data, status=200)

    if request.method == "POST":
        received_data = request.data
        serializer = serializers.ProductSerializer(data=received_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)
