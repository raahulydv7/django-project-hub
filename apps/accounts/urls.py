from django.urls import path
from . import views

urlpatterns = [
    path('root/', views.root, name='root'),
    path('register/', views.create_user, name='register'),
    path('login/', views.authenticate_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
