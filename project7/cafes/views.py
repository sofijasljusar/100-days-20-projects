from rest_framework import viewsets, views
from rest_framework.response import Response
from .models import Cafe
from .serializers import CafeSerializer
import random
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import CafeForm


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
        cafes = Cafe.objects.filter(location__icontains=location)  # icontains for partial or case-insensitive match
        if cafes:
            return Response({'cafes': CafeSerializer(cafes, many=True).data})
        return Response({'error': 'No cafes found at this location'}, status=404)


class CafeSearchListView(ListView):
    model = Cafe
    template_name = "cafes-list.html"
    context_object_name = "cafes_list"
    paginate_by = 3

    def get_queryset(self):
        query = self.request.GET.get('loc')
        if query:
            return Cafe.objects.filter(location__icontains=query)
        return Cafe.objects.none()



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


class CafeCreateView(CreateView):
    model = Cafe
    form_class = CafeForm
    template_name = 'cafe-form.html'
    success_url = reverse_lazy('home')


class CafeUpdateView(UpdateView):
    model = Cafe
    form_class = CafeForm
    template_name = 'cafe-form.html'
    success_url = reverse_lazy('home')


class CafeDeleteView(DeleteView):
    model = Cafe
    success_url = reverse_lazy('home')
