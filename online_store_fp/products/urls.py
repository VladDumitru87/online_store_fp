from django.urls import path
from .views import PostView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('list/', PostView.as_view(), name='product_list')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
