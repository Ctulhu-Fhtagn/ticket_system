from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()
    context = {
        'title': 'Tasks',
        'tasks': tasks,
    }
    return render(request, 'tickets/task_list.html', context)

def task_detail(request):
    context = {

    }
    return render(request, 'tickets/task_detail.html', context)
