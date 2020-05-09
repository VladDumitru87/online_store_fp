from django.views.generic import ListView
from .models import PostAdd


class PostView(ListView):
    model = PostAdd
    template_name = "product.html"
    context_object_name = "products"