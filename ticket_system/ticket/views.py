from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from ticket_system.ticket.models import Task, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ticket_system.ticket.forms import TaskForm, TaskEditForm



# Create your views here.
@login_required(login_url='/admin/login')
def task_list(request):
    tasks = Task.objects.all()

    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.executor = Client.get_random(Client.objects.filter(department=form.cleaned_data.get('department')))
            new_task.client = request.user.client
            new_task.save()
            form.save_m2m()

    elif request.method == 'GET':
        form = TaskForm()
    
    context = {
        'title': 'Tasks',
        'tasks': tasks,
        'form': form
    }
    return render(request, 'tickets/task_list.html', context)

@login_required(login_url='/admin/login')
def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
        'priority': Task.PRIORITY_CHOICES_DICT[task.priority],
        'status':  Task.STATUS_CHOICES_DICT[task.status],
    }
    
    return render(request, 'tickets/task_detail.html', context)
    

@login_required(login_url='/admin/login')
def task_edit(request, task_id):
    task = Task.objects.get(pk=task_id)
    
    if request.method == 'GET':
        form = TaskEditForm(instance=task)

    elif request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            task = form.save(commit=False)
            form.save_m2m()
            task.save()
            return redirect('task-detail',task_id=task.id)
            
    context = {
        'task': task,
        'form': form
    }
    
    return render(request, 'tickets/task_detail_edit.html', context)
    