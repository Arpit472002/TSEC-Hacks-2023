from django.urls import path
from .views import *
urlpatterns = [
    path('room-list/',RoomListCreateView.as_view(),name='room-list'),
    path('room-detail/<int:pk>/',RoomDetailView.as_view(),name='room-detail'),
    path('interested-users/',InterestedUserListView.as_view(),name='interested-users'),
    path('contact-us/<int:pk>/',ContactUsCreateView.as_view(),name='contact-us'),
]
