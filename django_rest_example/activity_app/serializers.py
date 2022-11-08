
from rest_framework import serializers
from .models import Activity
from django.contrib.auth.models import User

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, queryset=Activity.objects.all())
    class Meta:
        model = User
        fields = ['id', 'username', 'activities']
