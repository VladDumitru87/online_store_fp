from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import PostAdd


class PostListView(ListView):
    model = PostAdd
    template_name = "product_list.html"
    context_object_name = "products"


class PostCreateView(CreateView):
    model = PostAdd
    template_name = 'product_create.html'
    fields = '__all__'
    success_url = reverse_lazy('product_list')