from rest_framework import viewsets
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from django.shortcuts import render
from django.http import HttpResponse


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


def home_view(request):
    # This view function handles the request for the home page
    # and returns a simple HTTP response with a welcome message
    return HttpResponse("Welcome to the home page!")

