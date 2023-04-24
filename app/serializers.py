from rest_framework import serializers

from . import models


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Category
#         fields = '__all__'
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Product
#         fields = '__all__'


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)

    def create(self, validated_data):
        return models.Category.objects.create(name=validated_data['name'])

    def update(self, instance, validated_data):
        pass


class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    worth = serializers.IntegerField()
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return models.Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        pass

