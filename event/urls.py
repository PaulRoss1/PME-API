from django.urls import path, include
from event import views

urlpatterns = [
    path('events/all/', views.EventListAPIView.as_view(), name='event-list-all'),
    path('events/djs/', views.EventTypeListAPIView.as_view(), {'event_type': "DJ's"}, name='event-list-djs'),
    path('events/live-music/', views.EventTypeListAPIView.as_view(), {'event_type': 'Live Music'}, name='event-list-live-music'),
]