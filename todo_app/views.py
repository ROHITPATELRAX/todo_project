from rest_framework import generics, permissions
from rest_framework import authentication
from .models import TodoItem
from todo_app.serializers import TodoItemSerializer
from django.contrib import redirects
from rest_framework.exceptions import MethodNotAllowed

def errorHandler(requests):
    return redirects('auth/login/')

class TodoListView(generics.ListCreateAPIView,generics.CreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [authentication.TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]