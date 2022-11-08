
from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'info', 'when', 'owner_id']

    def create(self, validated_data):
        return Activity.objects.create(**validated_data)


class UserSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'activities']
