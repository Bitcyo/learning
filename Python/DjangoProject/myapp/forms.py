from django import forms

class CreateNewtask(forms.Form):
    title = forms.CharField(label="Task title", max_length=200, required=True)
    description = forms.CharField(label="Description of task", widget=forms.Textarea)
    
class CreateNewProject(forms.Form):
    name = forms.CharField(label="Project name", max_length=200, required=True)
  
    
