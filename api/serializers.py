from rest_framework import serializers


class CheckGameInputSerializer(serializers.Serializer):
    inputs = serializers.ListField(allow_empty=True)
    outputs = serializers.ListField( allow_empty=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
