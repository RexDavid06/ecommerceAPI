from django.shortcuts import render
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_available=True)
    filter_backends = [filters.SearchFilter, filters.OrderingFilter, DjangoFilterBackend]
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
    #enable search by name and description
    search_fields = ['name', 'description']
    #enable filtering by category and price
    filterset_fields = ['category', 'price']
    #enable ordering by price and created_at
    ordering_fields = ['price', 'created_at']
    ordering = ['-created_at']

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminUser]

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    permission_classes = [IsAdminUser]



