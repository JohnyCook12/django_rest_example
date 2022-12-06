from rest_framework import serializers
from .models import Person, Group
# from django.contrib.auth.models import User


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(min_value=1, max_value=160)

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        return Person.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'

    def create(self, validated_data):
        return Group.objects.create(**validated_data)
