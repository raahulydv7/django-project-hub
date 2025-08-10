from django.urls import path
from . import views

urlpatterns = [
    
    path('add-project/', views.create_project, name='add-project'),
    path('', views.projects, name='projects'),
]
