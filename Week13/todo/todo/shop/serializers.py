from rest_framework import serializers

from todo.auth_.serializers import UserSerializer
from todo.shop.models import OnlineProduct, Category


class CategorySerializer(serializers.ModelSerializer):

    owner = UserSerializer(read_only=True)

    class Meta:
        model = Category
        fields = '__all__'


class OnlineProductSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)

    class Meta:
        model = OnlineProduct
        fields = '__all__'
