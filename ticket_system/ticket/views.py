from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ticket_system.ticket.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ticket_system.ticket.forms import AddTaskForm

# Create your views here.
@login_required(login_url='/admin/login')
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
                # client=user,
                title=form.cleaned_data.get('title'),
                text=form.cleaned_data.get('text'),

            )
            new_task.save()
            new_task.tags.set(form.cleaned_data.get('tags')),
            context['form'] = AddTaskForm()
    elif request.method == 'GET':
        #if request.user == user:
        form = AddTaskForm()
        context['form'] = form
    return render(request, 'tickets/task_list.html', context)

@login_required(login_url='/admin/login')
def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
     }

    return render(request, 'tickets/task_detail.html', context)
