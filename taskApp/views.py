from django.shortcuts import render, redirect
from . import forms, models

# Create your views here.
def addTask(req):
    if req.method == 'POST':
         post_form = forms.TaskForm(req.POST)
         if post_form.is_valid():
              post_form.save()
              return redirect('home')
    else:
         post_form = forms.TaskForm()
    return render(req, 'addTask.html', {'form':post_form})


def editTask(req, id):
    post = models.Task.objects.get(pk=id)
    task_form = forms.TaskForm( instance = post)
    if req.method == 'POST':
         task_form = forms.TaskForm(req.POST, instance= post)
         if task_form.is_valid():
              task_form.save()
              return redirect('home')

    return render(req, 'addTask.html', {'form':task_form})

def deleteTask(req, id):
    post = models.Task.objects.get(pk=id)
    post.delete()
    return redirect('home')