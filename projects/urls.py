from django.urls import path
from projects.views import list_projects, project_detail, create_project

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", create_project, name="create_project"),
]
