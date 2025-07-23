from django.urls import path
from .views import CafeList, CafeDetail, CafeSearchListView

urlpatterns = [
    path('', CafeList.as_view(), name="home"),
    path('cafes/<int:pk>/', CafeDetail.as_view(), name="detail"),
    path('search/', CafeSearchListView.as_view(), name="search")
]
