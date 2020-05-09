from django.urls import path
from .views import PostView


urlpatterns = [
    path('list/', PostView.as_view(), name='product_list')
]
