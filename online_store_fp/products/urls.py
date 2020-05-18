from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

app_name = 'products'
urlpatterns = [
    path('list/', PostListView.as_view(), name='product_list'),
    path('create/', PostCreateView.as_view(), name='product_create'),
    path('detail/<int:pk>', PostDetailView.as_view(), name='product_detail'),
    path('update/<int:pk>', PostUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='product_delete'),
]
