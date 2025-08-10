from django.shortcuts import render,redirect,get
from .forms import ProjectForm
from .models import Project
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from functools import wraps
from django.contrib import messages

def role_required(allowed_roles):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request,*args, **kwargs):
            print("request.user.role: ",request.user.role)
            if request.user.role in allowed_roles:
                return view_func(request,*args, **kwargs)
            return HttpResponseForbidden("you don't have permission")
        return _wrapped_view
    return decorator


@login_required
@role_required(['ADMIN'])
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.save()
            form.save_m2m()
            messages.success(request,"Project Created successfully")
            return redirect('root')
        else:
            messages.error(request, "Unalbe to create project")
    else:
        form = ProjectForm()
    return render(request,"projects/create_project.html",{"form":form}) 

@login_required
@role_required(['ADMIN','PROJECT_MANAGER','TEAM_MEMBER'])
def projects(request):
    role = request.user.role

    if role == 'ADMIN':
        projects = Project.objects.all()
    elif role == 'PROJECT_MANAGER':
        projects = Project.objects.filter(manager=request.user)
    else:
        projects = Project.objects.filter(team_members=request.user)

    return render(request, "projects/projects.html", {"projects": projects})


@login_required
@role_required(['ADMIN','PROJECT_MANAGER','TEAM_MEMBER'])
def project_details(request,slug):
    project = get_
