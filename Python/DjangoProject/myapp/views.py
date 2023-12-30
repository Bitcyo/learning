#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp.models import Project, Tasks
from django.shortcuts import render, redirect , get_object_or_404
from .forms import CreateNewtask , CreateNewProject
from django.views.decorators.csrf import csrf_protect


@csrf_protect

# Create your views here.
def index(request):
    title = "hi nig**"
    return render(request, 'index.html',{
        'title': title 
    })

 
def hello(request,username):
    print (username)
    return HttpResponse("hi %s, hello there" %username) 

def about(request):
    return render(request, 'about.html')

def project(request):
    projects = list(Project.objects.all())
    return render(request, 'projects.html', {
        'projects': projects
    })
    
def tasks(request):
    tasks = Tasks.objects.all()
    return render(request, 'tasks.html',
                  {'tasks': tasks})
    
    
def create_task(request):
 if request.method == 'GET':
     #SHOW INTERFACE
    return render(request, "create_task.html", 
    {'form': CreateNewtask()
    }) 
 else:
    Tasks.objects.create(title= request.POST['title'],
    description= request.POST['description'], project_id=1)
    return redirect('tasks')

def create_project(request):
    if request.method == 'GET':        
        return render(request, "create_project.html", {
        'form': CreateNewProject()
        } )
    else:
        Project.objects.create(name= request.POST['name'],)
        return redirect('projects')
    
def project_details(request,id):
    Project = object.objects.get(id=id)
    get_object_or_404(Project, id=id)
    task = Tasks.objects.filter(project_id=id)
    return render(request,'detail.html',{
        'project': project,
        'task': tasks
    })