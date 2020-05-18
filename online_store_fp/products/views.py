from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PostAdd


class PostListView(ListView):
    model = PostAdd
    template_name = "products/product_list.html"
    context_object_name = "products"


class PostCreateView(CreateView):
    model = PostAdd
    template_name = 'products/product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class PostDetailView(DetailView):
    model = PostAdd
    template_name = 'products/product_detail.html'
    context_object_name = 'products'


class PostUpdateView(UpdateView):
    model = PostAdd
    template_name = 'products/product_update.html'
    context_object_name = 'products'
    fields = '__all__'
    success_url = reverse_lazy('product_list')


class PostDeleteView(DeleteView):
    model = PostAdd
    template_name = 'products/product_delete.html'
    context_object_name = 'products'
    success_url = reverse_lazy('product_list')