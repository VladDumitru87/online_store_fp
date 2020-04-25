from django.urls import path

from .views import user_login, user_logout, user_signup, UserProfile

urlpatterns = [
    path('login/', user_login, name="user-login"),
    path('logout/', user_logout, name="user-logout"),
    path('signup/', user_signup, name="user-signup"),
    path('user-profile/<int:pk>', UserProfile.as_view(), name="user-profile"),
]

