from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def addCategory(req):
    if req.method == 'POST':
         category_form = forms.CategoryForm(req.POST)
         if category_form.is_valid():
              category_form.save()
              return redirect('home')
    else:
         category_form = forms.CategoryForm()
    return render(req, 'addCategory.html', {'form':category_form})