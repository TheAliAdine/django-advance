from django.urls import path, include
from .. import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path(
        "registration",
        views.RegistrationApiView.as_view(),
        name="registration",
    ),
    path(
        "change-password/",
        views.ChangePasswordApiView.as_view(),
        name="change-password",
    ),
    # reset password
    path("test-email/", views.TestEmailSend.as_view(), name="test-email"),
    path(
        "activation/confirm/<str:token>",
        views.ActivationApiView.as_view(),
        name="activation",
    ),
    path(
        "activation/resend/",
        views.ActivationResentApiView.as_view(),
        name="activation-resend",
    ),
    # path("token/login",ObtainAuthToken.as_view(),name="token-login")
    path("token/login/", views.CustomAuthToken.as_view(), name="token-login"),
    path(
        "token/logout/",
        views.CustomDiscardAuthToken.as_view(),
        name="token-logout",
    ),
    path(
        "jwt/create/",
        views.CustomTokenObtainPair.as_view(),
        name="jwt-create",
    ),
    path("jwt/refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
    path("jwt/verify/", TokenVerifyView.as_view(), name="jwt-verify"),
]
