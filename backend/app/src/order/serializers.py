from rest_framework import serializers

class CreateOrderSerializer(serializers.Serializer):
	items = serializers.ListField(
		child=serializers.IntegerField()
	)