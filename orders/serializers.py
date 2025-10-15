from rest_framework import serializers
from .models import Cart, CartItem, Order, OrderItem
from products.serializers import ProductSerializer
from products.models import Product


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(write_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), source="product", write_only=True)

    class Meta:
        model =Cart
        fields = ["id", "product", "product_id", "quantity", "total_item_price"]


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "user", "items", "sum_total", "total_price"]

    def get_total_price(self, obj):
        return obj.sum_total()
    
    