from django import forms
from django.contrib.auth.models import User
from ticket_system.ticket.models import *


class AddTaskForm(forms.Form):
    title = forms.CharField(max_length=150)
    text = forms.CharField(max_length=2000)
    department = forms.ModelMultipleChoiceField(queryset=Department.objects.all())
    # priority = forms.ChoiceField(choices = Task.PRIORITY_CHOICES)
    # new_tag = forms.CharField(max_length=20, required=False)
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
    
    