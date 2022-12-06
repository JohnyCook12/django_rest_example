from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions, viewsets
from . import models
from .models import Person, Group
from .serializers import PersonSerializer, PersonCreateSerializer, GroupSerializer
from django.contrib.auth.models import User
from django.shortcuts import render


def index_view(request):
    return render(request, "index.html")

class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonCreateSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PersonGroupList(generics.ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer