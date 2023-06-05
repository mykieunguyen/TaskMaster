from django.shortcuts import render, redirect
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib.auth.decorators import login_required

# Create your views here.
# View to Create new task


@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_projects")

    else:
        form = TaskForm()

    context = {
        "form": form
    }

    return render(request, "tasks/create_task.html", context)

# View to see only tasks assigned to user


@login_required
def list_tasks(request):
    tasks = Task.objects.filter(assignee=request.user)

    context = {
        "tasks": tasks
    }

    return render(request, "tasks/list_tasks.html", context)
