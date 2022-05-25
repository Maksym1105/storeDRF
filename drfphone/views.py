from django.shortcuts import render
from rest_framework import generics

from .models import Phones
from .serializers import PhonesSerializer


class PhonesAPIView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
