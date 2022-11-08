from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api', views.api, name='api'),
    path('activity_list', views.activityList, name='activity_list'),
    path('activity_create', views.activityCreate, name='activity_create'),
    path('activity_delete/<str:id>/', views.activityDelete, name='activity_delete'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
]

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
    ]
