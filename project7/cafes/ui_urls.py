from django.urls import path
from .views import CafeList, CafeDetail, CafeSearchListView, CafeCreateView, CafeUpdateView, CafeDeleteView

urlpatterns = [
    path('', CafeList.as_view(), name="home"),
    path('cafes/<int:pk>/', CafeDetail.as_view(), name="detail"),
    path('cafes/search/', CafeSearchListView.as_view(), name="search"),
    path('cafes/add/', CafeCreateView.as_view(), name='add-cafe'),
    path('cafes/<int:pk>/edit/', CafeUpdateView.as_view(), name='edit-cafe'),
    path('cafes/<int:pk>/delete/', CafeDeleteView.as_view(), name='delete-cafe'),

]
