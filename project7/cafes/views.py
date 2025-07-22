from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import Cafe
from .serializers import CafeSerializer
import random
from django.views.generic import ListView, DetailView


class CafeViewSet(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class RandomCafeView(views.APIView):
    def get(self, request):
        cafes = list(Cafe.objects.all())
        if cafes:
            random_cafe = random.choice(cafes)
            return Response({'cafe': CafeSerializer(random_cafe).data})
        return Response({'error': 'No cafes found'}, status=404)


class CafeSearchView(views.APIView):
    def get(self, request):
        location = request.GET.get('loc')
        cafes = Cafe.objects.filter(location=location)
        if cafes:
            return Response({'cafes': CafeSerializer(cafes, many=True).data})
        return Response({'error': 'No cafes found at this location'}, status=404)
