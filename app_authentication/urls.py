from django.urls import path

from app_authentication import views

app_name = "auth"

urlpatterns = [
    path(
        "user_profile/",
        views.ShowProfilePageView.as_view(),
        name="user_profile",
    ),
    path(
        "user_profile/update/",
        views.UserProfileUpdate.as_view(),
        name="user_profile_update",
    ),
    path("login/", views.UserAuthentication.as_view(), name="login"),
    path("logout/", views.handle_user_logout, name="logout"),
    path("sing_up/", views.UserSignUp.as_view(), name="sing_up"),
]
