from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import User


class UsersListView(ListView):
    model = User
    template_name = 'users/users.html'


class UsersCreateView(CreateView):
    model = User
    fields = "__all__"
    template_name = 'users/user_create.html'

    def get_success_url(self):
        return reverse('users-list')


class UsersUpdateView(UpdateView):
    model = User
    fields = "__all__"
    template_name = "users/user_update.html"

    def get_success_url(self):
        return reverse('users-list')


class UsersDeleteView(DeleteView):
    model = User
    template_name = "users/user_delete.html"
    success_url = reverse_lazy('users-list')
