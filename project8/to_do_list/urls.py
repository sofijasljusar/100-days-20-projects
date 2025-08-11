from django.urls import path
from .views import (HomeView,
                    SignUpView,
                    LogInView,
                    HistoryMenuView,
                    AboutView,
                    DayDetailView,
                    MonthDetailView,
                    HabitCreateView,
                    HabitRecordToggleView,
                    ToDoHistoryView)
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LogInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('history/', HistoryMenuView.as_view(), name='history-menu'),
    path('about/', AboutView.as_view(), name='about'),

    path('day-detail/', DayDetailView.as_view(), name='day-detail'),
    path('month-detail/', MonthDetailView.as_view(), name='month-detail'),
    path('add-habit/', HabitCreateView.as_view(), name='add-habit'),
    path('toggle-habit/<int:habit_id>/<int:year>/<int:month>/<int:day>/',
         HabitRecordToggleView.as_view(), name='toggle-habit'),
    path('todo-history', ToDoHistoryView.as_view(), name="todo-history"),

]
