from django.db import models
from apps.accounts.models import CustomUser
from django.utils.text import slugify
class Project(models.Model):

    HOLD = 'HOLD'
    IN_PROGRESS = 'IN_PROGRESS'
    CANCELED = 'CANCELED'
    COMPLETED = 'COMPLETED'
    ONGOING = 'ONGOING'

    STATUS_CHOICES = [
        (HOLD, 'Hold'),
        (IN_PROGRESS, 'In progress'),
        (CANCELED, 'Canceled'),
        (COMPLETED, 'Completed'),
        (ONGOING, 'ongoing'),
    ]

    manager = models.ForeignKey(CustomUser, on_delete=models.CASCADE,limit_choices_to={'role':'PROJECT_MANAGER'},related_name='managed_project')
    team_members = models.ManyToManyField(CustomUser, related_name='projects',limit_choices_to={'role': 'TEAM_MEMBER'},blank=True)
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=50, unique=True , blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS_CHOICES,default=IN_PROGRESS)
    is_completed = models.BooleanField(default=False)
    completion_date  = models.DateField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.status} {self.created_at}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
    class Meta:
        ordering = ['-created_at']
