from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            'taskTitle': 'Title',
            'taskDesc': 'Description',
            'taskAssignDate': 'Assign Date',
        }