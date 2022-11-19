from django.urls import path, include
from . import views
from drf_yasg import openapi

urlpatterns = [
    path('activity_list', views.ActivityList.as_view(), name='activity_list'),
    path('activity_list/<int:pk>', views.ActivityDetail.as_view(), name='activity_detail'),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('', views.index_view),

]

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
    ]
