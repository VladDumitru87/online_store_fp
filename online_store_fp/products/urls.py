from django.urls import path
from .views import PostListView, PostCreateView


urlpatterns = [
    path('list/', PostListView.as_view(), name='product_list'),
    path('create/', PostCreateView.as_view(), name='product_create'),
]
