from django.urls import path
from .views import TodoListView, TodoDetailView, errorHandler

urlpatterns = [
    path('getall/', TodoListView.as_view(), name='todo-list'),
    path('get/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('create/', TodoListView.as_view(), name='todo-insertion'),
    path('update/<int:pk>/', TodoDetailView.as_view(), name='todo-updation'),
    path('delete/<int:pk>/', TodoDetailView.as_view(), name='todo-deletion'),
    # path(r'^$',errorHandler,name='unknown-routes')
]