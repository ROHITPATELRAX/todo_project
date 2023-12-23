from django.urls import path
from .views import AuthRegister, AuthLogin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', AuthRegister.as_view(), name='auth-register'),
    path('', AuthLogin.as_view(), name='auth-login'),
]
