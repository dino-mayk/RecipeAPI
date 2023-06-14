from rest_framework import serializers

from apis.models import FoodType


class FoodTypeSerializer(serializers.HyperlinkedModelSerializer):

    title = serializers.CharField(
        max_length=150,
    )

    def create(self, validated_data):
        food_type = FoodType.objects.create(**validated_data)
        return food_type

    class Meta:
        model = FoodType
        fields = [
            'id',
            'title',
        ]
