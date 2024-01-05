from django.db.models import Q

from django.shortcuts import render
from django.http import Http404
from rest_framework import serializers

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView

from datetime import date, timedelta

from .models import Event
from .serializers import EventSerializer


class EventListAPIView(APIView):
    def get(self, request, format=None):
        queryset = Event.objects.all()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)

class EventTypeListAPIView(APIView):
    def get(self, request, event_type, format=None):
        queryset = Event.objects.filter(event_type=event_type)
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)
