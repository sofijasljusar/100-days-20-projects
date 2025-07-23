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


class CafeList(ListView):
    queryset = Cafe.objects.all()
    template_name = "cafes-list.html"
    context_object_name = 'cafes_list'
    paginate_by = 5


class CafeDetail(DetailView):
    model = Cafe
    template_name = "cafe-detail.html"
    context_object_name = "cafe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cafe = self.get_object()
        context['features'] = [
            {'label': 'Wi-Fi', 'value': cafe.has_wifi},
            {'label': 'Sockets', 'value': cafe.has_sockets},
            {'label': 'Toilet', 'value': cafe.has_toilet},
            {'label': 'Can take calls', 'value': cafe.can_take_calls}
        ]
        return context
