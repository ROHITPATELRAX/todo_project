from rest_framework import generics, permissions
from rest_framework import authentication
from .models import TodoItem
from todo_app.serializers import TodoItemSerializer
from django.contrib import redirects

def errorHandler(requests):
    return redirects('auth/login/')

class TodoListView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    authentication_classes = [authentication.TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]

class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    # authentication_classes = [TokenAuthentication] 
    permission_classes = [permissions.IsAuthenticated]
