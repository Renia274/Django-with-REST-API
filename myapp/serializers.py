from rest_framework import serializers
from .models import Category, Product

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Specify the category model to serialize
        fields = '__all__'  # Include all fields from the Category model in the serialization


# Product Serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product  #Specify product model to serialize
        fields = '__all__'  # Include all fields from the Product model in the serialization

