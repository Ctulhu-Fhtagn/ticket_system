from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from ticket_system.ticket.models import *
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def task_list(request):
    tasks = Task.objects.all()
    context = {
        'title': 'Tasks',
        'tasks': tasks,
    }
    return render(request, 'tickets/task_list.html', context)

@login_required
def task_detail(request):
    context = {

    }
    return render(request, 'tickets/task_detail.html', context)
