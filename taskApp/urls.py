from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.addTask, name='add-task'),
    path('editTask/<int:id>', views.editTask, name='edit-task'),
    path('deleteTask/<int:id>', views.deleteTask, name='delete-task'),
]
