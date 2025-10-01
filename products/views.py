from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework import generics

# Create your views here.

