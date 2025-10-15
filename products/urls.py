from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('category/create/', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/update/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-update'),
    path('', views.ProductListView.as_view(), name='products'),
    path('create/', views.ProductCreateView.as_view(), name='product-create'),
    path('update/<int:id>/', views.ProductRetrieveUpdateDestroyView.as_view(), name='product-update')
]