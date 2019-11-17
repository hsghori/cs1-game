from rest_framework import serializers


class CheckGameInputSerializer(serializers.Serializer):
    inputs = serializers.ListField(
        child=serializers.ListField(allow_empty=True),
    )
    outputs = serializers.ListField(
        child=serializers.ListField(allow_empty=True),
    )

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    def validate(self, attrs):
        if len(attrs['inputs']) != len(attrs['outputs']):
            raise serializers.ValidationError('There must be the same number of inputs as outputs.')
        return attrs
