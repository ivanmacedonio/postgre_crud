from django.urls import path
from .views import *
urlpatterns = [

    path('', list_tasks),
    path('new/', create_task),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
]