from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from projects.forms import ProjectForm, Search
from taggit.models import Tag
from calendar import HTMLCalendar
from datetime import date

# Create your views here.
# View to show all projects in db


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    top_tags = Project.tags.most_common()[:10]

    context = {
        "projects": projects,
        "top_tags": top_tags,
    }

    return render(request, "projects/list.html", context)


# View to show details of specific project
@login_required
def project_detail(request, id):
    project_instance = get_object_or_404(Project, id=id)

    context = {
        "project": project_instance,
    }

    return render(request, "projects/project_detail.html", context)


# View to create new project


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = ProjectForm()

    context = {
        "form": form,
    }

    return render(request, "projects/create_project.html", context)


# TAGS View: Show Project with matching tag
@login_required
def show_tagged_project(request, id):
    projects = Project.objects.filter(tags__id=id)

    context = {
        "projects": projects,
    }

    return render(request, "projects/tag_project_list.html", context)

# View for Base HTML Template


@login_required
def base_template(request):
    projects = Project.objects.filter(owner=request.user)

    TODAY = date.today()
    year = TODAY.year
    month = TODAY.month

    cal = HTMLCalendar().formatmonth(year, month)
    context = {
        "projects": projects,
        "calendar": cal,
        "year": year,
        "month": month,
    }

    return render(request, "base.html", context)

# View for Search Results


@login_required
def show_search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        projects = Project.objects.filter(name=searched)
        tasks = Task.objects.filter(name=searched)

        context = {
            "searched": searched,
            "projects": projects,
            "tasks": tasks,
        }
        return render(request, "projects/search_results.html", context)

    else:
        return render(request, "projects/search_results.html")
