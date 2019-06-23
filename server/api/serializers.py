from rest_framework import serializers

from .models import Category, Item, AuditLog


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    metadata = serializers.JSONField(required=False)
    rank = serializers.IntegerField(read_only=True)

    class Meta:
        model = Item
        fields = '__all__'


class AuditLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = AuditLog
        fields = '__all__'
