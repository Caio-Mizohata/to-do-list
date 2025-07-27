from django.contrib import admin
from django.urls import path
from to_do.views import TaskListView, create_task, delete_task, update_task 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TaskListView.as_view(), name='task_list'),
    path('tasks/create/', create_task, name='create_task'),
    path('tasks/delete/<int:pk>/', delete_task, name='delete_task'),
    path('tasks/update/<int:pk>/', update_task, name='update_task'),
]
