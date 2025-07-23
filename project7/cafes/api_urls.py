from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CafeViewSet, RandomCafeView, CafeSearchView

router = DefaultRouter()
router.register(r'cafes', CafeViewSet)

urlpatterns = [path('', include(router.urls)),
               path('random/', RandomCafeView.as_view(), name="random-api"),
               path('search/', CafeSearchView.as_view(), name="search-api")]
