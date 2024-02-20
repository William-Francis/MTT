from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import django_filters
import json

# Create your views here.
from django.http import Http404, HttpResponse
from core.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.reverse import reverse
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import User


def index(request):
    return HttpResponse("Hello, world. You're at the MTT index.")


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
