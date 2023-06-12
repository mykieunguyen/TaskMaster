from django.urls import path
from tasks.views import create_task, list_tasks, completed_tasks

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("completed/", completed_tasks, name="completed_tasks"),

]
