from rest_framework import serializers


class ProductCreatePayloadSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)


class ProductUpdatePayloadSerializer(serializers.Serializer):
    is_active = serializers.BooleanField(default=True)
