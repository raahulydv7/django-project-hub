from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ADMIN = 'ADMIN'
    PROJECT_MANAGER = 'PROJECT_MANAGER'
    TEAM_MEMBER = 'TEAM_MEMBER'

    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (PROJECT_MANAGER, 'Project Manager'),
        (TEAM_MEMBER, 'Team Member'),
    ]

    role= models.CharField(max_length=20,choices=ROLE_CHOICES,default=TEAM_MEMBER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar  = models.ImageField(upload_to='profile/',default='avtar.jpg')
    fname = models.CharField(max_length=50,null=True,blank=True)
    lname = models.CharField(max_length=50,null=True,blank=True)
    contact = models.CharField(max_length=10,null=True,blank=True)
    
    def __str__(self):
        return f"{self.user.username} {self.fname} {self.lname}"