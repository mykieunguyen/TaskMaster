from django.shortcuts import render, redirect, get_object_or_404
from projects.models import Project
from django.contrib.auth.decorators import login_required

# Create your views here.
# View to show all projects in db


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)

    context = {
        "projects": projects
    }

    return render(request, "projects/list.html", context)


# View to show details of specific project
@login_required
def project_detail(request, id):
    project_instance = get_object_or_404(Project, id=id)

    context = {
        "project": project_instance
    }

    return render(request, "projects/project_detail.html", context)
