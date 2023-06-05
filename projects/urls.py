from django.urls import path
from projects.views import list_projects, project_detail

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project")
]
