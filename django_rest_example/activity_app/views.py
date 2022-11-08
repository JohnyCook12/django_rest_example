from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework import mixins, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ActivitySerializer
from .models import Activity
from django.contrib.auth.models import User
from .serializers import UserSerializer

# Create your views here.
def index(request):
    return HttpResponse('Welcome')


@api_view(['GET'])
def api(request):
    api_urls = {
        'List' : '/activity_list/',
        'Create' : '/activity-create/'
    }
    return Response(api_urls)

@api_view(['GET'])
def activityList(request):
    activities = Activity.objects.all()
    serializer = ActivitySerializer(activities, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def activityCreate(request):
    serializer = ActivitySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response("Missing some data")

@api_view(['DELETE'])
def activityDelete(request, id):
    activity = Activity.objects.get(id=id)
    activity.delete()
    return Response('Item deleted')

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer