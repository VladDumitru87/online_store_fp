from django.urls import path
from . import views as user_views


app_name = 'accounts'
urlpatterns = [
    path('', user_views.home, name='index'),
]

