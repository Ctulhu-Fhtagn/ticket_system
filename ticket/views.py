from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import AddTaskForm

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    form = AddTaskForm()
    context = {
        'title': 'Tasks',
        'tasks': tasks,
        'form': form
    }
    if request.method == 'POST':
        form = AddTaskForm(request.POST)
        if form.is_valid():
            new_task = Task(
                user=user,
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),

            )
            new_task.save()
            new_task.tags.set(form.cleaned_data.get('tags')),
            context['form'] = AddTaskForm()
    elif request.method == 'GET':
        #if request.user == user:
        form = AddTaskForm(),
        context['form'] = form
    return render(request, 'tickets/task_list.html', context)

def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'title': task.title,
        'task': task,
    }
    return render(request, 'tickets/task_detail.html', context)
