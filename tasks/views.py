from django.shortcuts import render,HttpResponse,redirect
from .models import *

def list_tasks(request):
    tasks= Task.objects.all()
    return render(request, 'list_tasks.html', {
        "tasks": tasks
    })

def create_task(request):
    task= Task(title=request.POST['title'], description=request.POST['description'])
    task.save()
    return redirect('/tasks/')

def delete_task(request,pk):
    task = Task.objects.filter(id=pk)
    task.delete()
    return redirect('/tasks/')