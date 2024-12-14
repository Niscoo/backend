from rest_framework import serializers
from .models import Category, Product, Order, OrderItem, ProductImage, Review, User, ShippingAddress, Promotion
from dj_rest_auth.serializers import UserDetailsSerializer



class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta:
        model = User  
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # Or explicitly list the fields you want to include

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # If there's an image, ensure the full URL is returned
        if instance.image:
            representation['image'] = instance.image.url  # Add the full URL for the image
        return representation

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = '__all__'