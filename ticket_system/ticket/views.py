from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import UpdateView
from ticket_system.ticket.models import Task, Client
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from ticket_system.ticket.forms import TaskForm



# Create your views here.
@login_required(login_url='/admin/login')
def task_list(request):
    tasks = Task.objects.all()
    # form = AddTaskForm()
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            # new_task = Task(
            #     client=request.user.client,
            #     executor=Client.get_random(Client.objects.filter(department=form.cleaned_data.get('department')[0])),
            #     title=form.cleaned_data.get('title'),
            #     text=form.cleaned_data.get('text'),
            #     department=form.cleaned_data.get('department')[0],
            # )
            # new_task.save()
            new_task = form.save(commit=False)
            # import pdb; pdb.set_trace()
            new_task.executor = Client.get_random(Client.objects.filter(department=form.cleaned_data.get('department')))
            new_task.client = request.user.client
            new_task.save()
            form.save_m2m()
            # context['form'] = AddTaskForm()
    elif request.method == 'GET':
        form = TaskForm()
        # context['form'] = form
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
    context = {
        'task': task,
        'priority': Task.PRIORITY_CHOICES_DICT[task.priority],
        'status':  Task.STATUS_CHOICES_DICT[task.status],
    }
    
    return render(request, 'tickets/task_detail_edit.html', context)
    