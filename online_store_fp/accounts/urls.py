from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('', user_views.home, name='index'),
    path('signup', user_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name="logout"),
    path('user', user_views.user, name='user'),
]

