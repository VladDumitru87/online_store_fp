from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import UsersListView, UsersCreateView, UsersUpdateView, UsersDeleteView

app_name = 'users'
urlpatterns = [
    path('', login_required(UsersListView.as_view()), name="users-list"),
    path('create/', login_required(UsersCreateView.as_view()), name="user-create"),
    path('update/<int:pk>/', login_required(UsersUpdateView.as_view()), name="user-update"),
    path('delete/<int:pk>/', login_required(UsersDeleteView.as_view()), name="user-delete"),
]

