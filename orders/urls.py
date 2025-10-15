from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartView.as_view(), name='cart-details'), 
    path('cart/add/', views.AddCartView.as_view(), name='cart-add'),
    path('cart/item/<int:pk>/', views.UpdateCartItemView.as_view(), name='update-cart'),
]