from django.urls import path
from .views import CafeList, CafeDetail, CafeSearchListView, CafeCreateView, CafeUpdateView, CafeDeleteView, SignUpView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', CafeList.as_view(), name="home"),
    path('cafes/<int:pk>/', CafeDetail.as_view(), name="detail"),
    path('cafes/search/', CafeSearchListView.as_view(), name="search"),
    path('cafes/add/', CafeCreateView.as_view(), name='add-cafe'),
    path('cafes/<int:pk>/edit/', CafeUpdateView.as_view(), name='edit-cafe'),
    path('cafes/<int:pk>/delete/', CafeDeleteView.as_view(), name='delete-cafe'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

]
