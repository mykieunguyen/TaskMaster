from django.urls import path
from tasks.views import create_task, list_tasks, completed_tasks, edit_task

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("completed/", completed_tasks, name="completed_tasks"),
    path("<int:id>/edit/", edit_task, name="edit_task"),

]
