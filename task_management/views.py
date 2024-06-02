from django.shortcuts import render
from taskApp.models import Task

def home(req):
    data = Task.objects.all()
    return render(req, 'index.html', {'data':data})