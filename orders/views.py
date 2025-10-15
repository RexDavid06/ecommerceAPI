from django.shortcuts import render
from rest_framework import generics
from .serializers import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Cart, CartItem, Order, OrderItem
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class CartView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class AddCartView(generics.CreateAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class UpdateCartItemView(generics.UpdateAPIView, generics.DestroyAPIView):
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]
    queryset = CartItem.objects.all()


class CreateOrderView(generics.CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        cart = request.user.cart  # assuming each user has one cart
        if not cart.items.exists():
            return Response({"detail": "Your cart is empty."}, status=status.HTTP_400_BAD_REQUEST)

        order = Order.objects.create(user=request.user)
        for item in cart.items.all():
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        order.calculate_total()
        cart.items.all().delete()  # clear cart after order

        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)