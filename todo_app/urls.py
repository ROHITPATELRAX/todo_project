from django.urls import path
from .views import TodoListView

urlpatterns = [
    path('getall/', TodoListView.as_view(), name='todo-list'),
    path('get/<int:pk>/', TodoListView.as_view(), name='todo-detail'),
    path('create/', TodoListView.as_view(), name='todo-insertion'),
    path('update/<int:pk>/', TodoListView.as_view(), name='todo-updation'),
    path('delete/<int:pk>/', TodoListView.as_view(), name='todo-deletion'),
    # path(r'^$',errorHandler,name='unknown-routes')
]