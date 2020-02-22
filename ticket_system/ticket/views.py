from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ticket_system.ticket.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

# Create your views here.
@login_required(login_url='/admin/login')
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'title': 'Tasks',
        'tasks': tasks,
    }
    return render(request, 'tickets/task_list.html', context)

@login_required(login_url='/admin/login')
def task_detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
     }

    return render(request, 'tickets/task_detail.html', context)
