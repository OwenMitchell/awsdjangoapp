from rest_framework import serializers
from .models import Product
import json


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id',
                  'name',
                  'price',
                  'sizes',
                  'image']
