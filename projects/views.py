from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from projects.models import Project
from tasks.models import Task
from accounts.models import UserProfile
from projects.forms import ProjectForm, Search
from taggit.models import Tag
from calendar import HTMLCalendar
from datetime import date, datetime
import pytz

# Create your views here.
# View to show all projects in db


@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user, status="Active")
    top_tags = Project.tags.most_common()[:10]
    completed_projects = Project.objects.filter(status="Completed")
    completed_tasks = Task.objects.filter(is_completed=True)
    urgent_tasks = Task.objects.filter(is_completed=False).order_by('due_date')
    user_avatar = UserProfile.objects.get(user=request.user)

    # Calculte most urgent task
    TODAY = datetime.now(pytz.timezone('UCT'))
    urgent_task = "None"
    days_countdown = 0
    for task in urgent_tasks:
        if TODAY < task.due_date:
            urgent_task = task
            days_countdown = (task.due_date - TODAY).days
            break
        else:
            continue

    context = {
        "projects": projects,
        "top_tags": top_tags,
        "projects": projects,
        "completed_projects": completed_projects,
        "completed_tasks": completed_tasks,
        'urgent_task': urgent_task,
        "days_countdown": days_countdown,
        "user_avatar": user_avatar,
    }

    return render(request, "projects/list.html", context)


# View to show Completed Projects
@login_required
def completed_projects(request):
    projects = Project.objects.filter(owner=request.user, status="Completed")
    top_tags = Project.tags.most_common()[:10]
    completed_projects = Project.objects.filter(status="Completed")
    completed_tasks = Task.objects.filter(is_completed=True)
    urgent_tasks = Task.objects.filter(is_completed=False).order_by('due_date')
    user_avatar = UserProfile.objects.get(user=request.user)

    # Calculte most urgent task
    TODAY = datetime.now(pytz.timezone('UCT'))
    urgent_task = "None"
    days_countdown = 0
    for task in urgent_tasks:
        if TODAY < task.due_date:
            urgent_task = task
            days_countdown = (task.due_date - TODAY).days
            break
        else:
            continue

    context = {
        "projects": projects,
        "top_tags": top_tags,
        "projects": projects,
        "completed_projects": completed_projects,
        "completed_tasks": completed_tasks,
        'urgent_task': urgent_task,
        "days_countdown": days_countdown,
        "user_avatar": user_avatar,
    }

    return render(request, "projects/completed_projects.html", context)

# View to show details of specific project


@login_required
def project_detail(request, id):
    project_instance = get_object_or_404(Project, id=id)
    completed_projects = Project.objects.filter(status="Completed")
    completed_tasks = Task.objects.filter(is_completed=True)
    urgent_tasks = Task.objects.filter(is_completed=False).order_by('due_date')
    user_avatar = UserProfile.objects.get(user=request.user)

    TODAY = datetime.now(pytz.timezone('UCT'))
    urgent_task = "None"
    days_countdown = 0
    for task in urgent_tasks:
        if TODAY < task.due_date:
            urgent_task = task
            days_countdown = (task.due_date - TODAY).days
            break
        else:
            continue

    context = {
        "project": project_instance,
        "completed_projects": completed_projects,
        "completed_tasks": completed_tasks,
        'urgent_task': urgent_task,
        "days_countdown": days_countdown,
        "user_avatar": user_avatar,
    }

    return render(request, "projects/project_detail.html", context)


# View to edit project


@login_required
def edit_project(request, id):
    project_instance = get_object_or_404(Project, id=id)
    user_avatar = UserProfile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project_instance)
        if form.is_valid():
            form.save()
            return redirect("show_project", id=id)

    else:
        form = ProjectForm(instance=project_instance)

    context = {
        "project_form": form,
        "user_avatar": user_avatar,

    }
    return render(request, 'projects/edit_project.html', context)


# View to create new project


@login_required
def create_project(request):
    user_avatar = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = ProjectForm()

    context = {
        "form": form,
        "user_avatar": user_avatar,

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


@login_required
def show_search_result(request):
    if request.method == "POST":
        searched = request.POST['searched']
        tasks = Task.objects.filter(name__icontains=searched)
        tags = Tag.objects.filter(name__icontains=searched)
        filter_set = Q(name__icontains=searched) | Q(tags__in=tags)
        projects = Project.objects.filter(filter_set).distinct()

        context = {
            "searched": searched,
            "projects": projects,
            "tasks": tasks,
        }
        return render(request, "projects/search_results.html", context)

    else:
        return render(request, "projects/search_results.html")


# Delete Project View
@login_required
def delete_project(request, id):
    project_instance = Project.objects.get(id=id)
    project_instance.delete()
    return redirect("list_projects")
