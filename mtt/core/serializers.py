from django.db import transaction
from django.forms import ValidationError
from rest_framework.response import Response
from rest_framework import serializers
 
from .models import User
from io import BytesIO
import csv
from rest_framework import status

 

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "created", "modified"]
