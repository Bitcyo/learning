from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about" ),
    path('hello/<str:username>', views.hello, name="hello"  ),
    path('projects/', views.project, name="project" ),
    path('projects/<int:id>', views.project_details, name="project_details" ),
    path('tasks/' , views.tasks, name="tasks" ),
    path('create_task/', views.create_task, name="create_task" ),
    path('create_project/', views.create_project, name="create_project" ),
]