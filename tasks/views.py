from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Task
from tasks.forms import TaskForm
from projects.models import Project
from datetime import datetime
import pytz
from accounts.models import UserProfile

from django.contrib.auth.decorators import login_required


# Create your views here.
# View to Create new task


@login_required
def create_task(request):
    user_avatar = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = TaskForm()

    context = {
        "form": form,
        "user_avatar": user_avatar,

    }

    return render(request, "tasks/create_task.html", context)


# View to see only tasks assigned to user


@login_required
def list_tasks(request):
    tasks = Task.objects.filter(assignee=request.user, is_completed=False)
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
        "tasks": tasks,
        "completed_projects": completed_projects,
        "completed_tasks": completed_tasks,
        'urgent_task': urgent_task,
        "days_countdown": days_countdown,
        "user_avatar": user_avatar,
    }

    return render(request, "tasks/list_tasks.html", context)

# View for Completed Task


@login_required
def completed_tasks(request):
    tasks = Task.objects.filter(assignee=request.user, is_completed=True)
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
        "tasks": tasks,
        "completed_projects": completed_projects,
        "completed_tasks": completed_tasks,
        'urgent_task': urgent_task,
        "days_countdown": days_countdown,
        "user_avatar": user_avatar,
    }

    return render(request, "tasks/completed_tasks.html", context)

# Edit Task


@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id)
    user_avatar = UserProfile.objects.get(user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("show_my_tasks")

    else:
        form = TaskForm(instance=task)

    context = {
        'task_form': form,
        "user_avatar": user_avatar,

    }

    return render(request, "tasks/edit_task.html", context)


# Delete Task
@login_required
def delete_task(request, id):
    task_instance = Task.objects.get(id=id)
    task_instance.delete()
    return redirect("show_my_tasks")
