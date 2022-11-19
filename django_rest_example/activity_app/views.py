from rest_framework import generics, permissions
from .models import Activity
from django.contrib.auth.models import User
from django.shortcuts import render
from .serializers import UserSerializer, ActivitySerializer


def index_view(request):
    return render(request, "index.html")


class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ActivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.IsAdminUser]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
