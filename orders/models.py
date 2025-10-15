from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='cart')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def sum_total(self):
        return sum(item.total_item_price() for item in self.items.all())


    def __str__(self):
        return f"{self.user.username}'s CART"
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_item_price(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name} * {self.quantity}"


class Order(models.Model):
    STATUS_CHOICES = (
        ("PENDING", "Pending"),
        ("PROCESSING", "Processing"),
        ("SHIPPED", "Shipped"),
        ("DELIVERED", "Delivered"),
        ("CANCELLED", "Cancelled"),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default="PENDING")
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"
    
    def calculate_total(self):
        total = sum(item.total_item_price() for item in self.items.all())
        self.total_price = total
        self.save()
        return total
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='orderItems', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def subtotal(self):
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.product.name}  x {self.quantity}"