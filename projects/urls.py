from django.urls import path
from projects.views import list_projects, project_detail, create_project, show_tagged_project, show_search_result, completed_projects

urlpatterns = [
    path("", list_projects, name="list_projects"),
    path("<int:id>/", project_detail, name="show_project"),
    path("create/", create_project, name="create_project"),
    path("tags/<int:id>/", show_tagged_project, name="show_tagged_project"),
    path("search/", show_search_result, name='show_search_results'),
    path("completed/", completed_projects, name="completed_projects"),

]
