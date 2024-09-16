from rest_framework import serializers
from .models import (Products)


class Products_serializers(serializers.ModelSerializer):

    class Meta:

        model = Products
        fields = '__all__'
        