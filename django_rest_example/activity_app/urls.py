from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('activity_list', views.activityList, name='activity_list'),
    path('activity_create', views.activityCreate, name='activity_create'),
    path('activity_delete/<str:id>/', views.activityDelete, name='activity_delete'),
]