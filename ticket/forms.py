from django import forms
from django.contrib.auth.models import User
from .models import Tag, Department, Task


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.Textarea)
    text = forms.CharField(max_length=2000, widget=forms.Textarea)
    new_tag = forms.CharField(max_length=20, widget=forms.Textarea)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    department = forms.ModelMultipleChoiceField(queryset=Department.objects.all(), required=False)
    priority_client = forms.ChoiceField(choices = Task.PRIORITY_CHOICES)
