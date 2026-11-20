from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def taskView(request):
    tasks = Task.objects.exclude(completion_status=True)
    completed_tasks = Task.objects.filter(completion_status=True)

    context = {
        "tasks": tasks,
        "completed_tasks": completed_tasks
    }

    return render(request=request, template_name="tasks.html", context=context)

def taskComplete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if task.completion_status == False:
        task.completion_status = True
    else:
        task.completion_status = False
    task.save()
    return redirect("all_tasks")