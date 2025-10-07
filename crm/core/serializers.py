from rest_framework import serializers


class ErrorResponseSerializer(serializers.Serializer):
    request_id = serializers.CharField()
    code = serializers.CharField()
    message = serializers.CharField()
