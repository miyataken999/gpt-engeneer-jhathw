from rest_framework import serializers
from .models import Product, Evaluation

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'purchase_place', 'purchase_price', 'quality_state', 'email_state']

class EvaluationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evaluation
        fields = ['id', 'product', 'rating', 'comment']