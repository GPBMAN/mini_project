from django.urls import path
from . import views as v

urlpatterns = [
    path('tasks/', v.taskView, name="all_tasks"),
    path('complete/<int:pk>/', v.taskComplete, name="task_complete")
]