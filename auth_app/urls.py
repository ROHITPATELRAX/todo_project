from django.urls import path
from .views import AuthRegister, AuthLogin

urlpatterns = [
    path('register/', AuthRegister.as_view(), name='auth-register'),
    path('', AuthLogin.as_view(), name='auth-login'),
]
