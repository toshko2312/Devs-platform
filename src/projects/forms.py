from django.forms import ModelForm
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ('vote_total', 'vote_ratio')
