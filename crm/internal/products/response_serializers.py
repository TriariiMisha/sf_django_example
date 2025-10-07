from rest_framework import serializers


class ProductDtoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    is_active = serializers.BooleanField(default=True)

    id = serializers.UUIDField()
    created_at = serializers.IntegerField()
    updated_at = serializers.IntegerField()
    created_by = serializers.CharField(max_length=256)
