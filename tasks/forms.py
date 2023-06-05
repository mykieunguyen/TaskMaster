from django.forms import ModelForm
from tasks.models import Task

# Form to create new Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = (
            "name",
            "start_date",
            "due_date",
            "project",
            "assignee",
        )
