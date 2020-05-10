from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import user_login, user_logout, user_signup, UserProfile, UsersDelete


app_name = 'accounts'
urlpatterns = [
    path('login/', user_login, name="user-login"),
    path('logout/', user_logout, name="user-logout"),
    path('signup/', user_signup, name="user-signup"),
    path('user/<int:pk>', UserProfile.as_view(), name="user-profile"),
    path('delete/<int:pk>/', login_required(UsersDelete.as_view()), name="user-delete"),
]

