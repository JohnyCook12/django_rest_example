from django.urls import path, include
from . import views

urlpatterns = [
    path('people', views.PersonList.as_view(), name='person_list'),
    path('people/<int:pk>', views.PersonDetail.as_view(), name='person'),
    path('groups', views.GroupList.as_view(), name='group_list'),
    path('groups/<int:pk>', views.GroupDetail.as_view(), name='group'),
    path('people_groups', views.PersonGroupList.as_view(), name='person_group'),

    path('', views.index_view),

]

urlpatterns += [
    path('api-auth', include('rest_framework.urls'))
    ]

