from django.urls import path
from .views import CafeList, CafeDetail

urlpatterns = [
    path('', CafeList.as_view(), name="home"),
]
