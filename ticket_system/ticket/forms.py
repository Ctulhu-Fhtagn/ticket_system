from django import forms
from django.contrib.auth.models import User
from ticket_system.ticket.models import *
from crispy_forms.helper import FormHelper
from django.urls import reverse
from crispy_forms.layout import Submit



class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['executor','department','priority','status','tag']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        if self.instance.id:
            self.helper.form_action = reverse('task-edit', args=[self.instance.id])
        else:
            self.helper.form_action = reverse('task-list')
        self.helper.add_input(Submit('submit', 'Submit'))


class TaskForm(TaskEditForm):
    class Meta:
        model = Task
        fields = ['title', 'text', 'department', 'tag']    
