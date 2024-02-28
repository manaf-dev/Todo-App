from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Task
from .forms import AddTask

# Create your views here.
def home(request):
    tasks = Task.objects.filter(user=request.user.id)
    context = {'tasks': tasks}
    return render(request, 'Todo/home.html', context)

@login_required
def taskDetail(request, pk):
    task = get_object_or_404(Task, id=pk)
    context = {'task':task}
    return render(request, 'Todo/task_detail.html', context)


@login_required
def addTask(request):
    if request.method == 'POST':
        form = AddTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'New task has been added!')
            return redirect('home')
        else:
            messages.error(request, 'Your title is invalid!')
            return redirect('add-task')
    else:
        form = AddTask()
    
    context = {'form':form}
    return render(request, 'Todo/task_form.html', context)


@login_required
def updateTask(request, pk):
    task = get_object_or_404(Task, id=pk)
    if request.method == 'POST':
        form = AddTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task has been update!')
            return redirect('home')
    else:
        form = AddTask(instance=task)
    
    context = {'form':form}
    return render(request, 'Todo/task_form.html', context)


@login_required
def deleteTask(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('home')
    return render(request, 'Todo/confirm_delete.html', {'task':task})


@login_required
def completeTask(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        if task.is_complete:
            task.is_complete = False
            task.save()
            return redirect('home')
        else:
            task.is_complete = True
            task.save()
            return redirect('home')
    return redirect('home')


@login_required
def pendingTask(request, pk):
    if request.method == 'POST':
        task = get_object_or_404(Task, pk=pk)
        if task.is_valid():
            task.is_complete = False
            task.save()
            return redirect('home')
    return redirect('home')