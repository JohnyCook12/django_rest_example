from django.urls import path, include
from . import views
from drf_yasg import openapi

urlpatterns = [
    path('person_list', views.PersonList.as_view(), name='person_list'),
    path('person/<int:pk>', views.PersonDetail.as_view(), name='person'),
    path('group_list', views.GroupList.as_view(), name='group_list'),
    path('group/<int:pk>', views.GroupDetail.as_view(), name='group'),
    path('', views.index_view),

]

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
    ]
