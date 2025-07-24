from django.urls import path
from .views import CafeList, CafeDetail, CafeSearchListView, CafeCreateView

urlpatterns = [
    path('', CafeList.as_view(), name="home"),
    path('cafes/<int:pk>/', CafeDetail.as_view(), name="detail"),
    path('cafes/search/', CafeSearchListView.as_view(), name="search"),
    path('cafes/add/', CafeCreateView.as_view(), name='add-cafe'),

]
