from django.forms import ModelForm
from projects.models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = (
            "name",
            "description",
            "owner",
            "deadline",
            "status",
            "tags",
        )


class Search(forms.Form):
    search_item = forms.CharField(max_length=150)
