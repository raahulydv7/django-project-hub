from django import forms
from .models import Project
from apps.accounts.models import CustomUser

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['manager','team_members','title','description','status','is_completed','completion_date']


    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['manager'].queryset = CustomUser.objects.filter(role='PROJECT_MANAGER')
        self.fields['team_members'].queryset = CustomUser.objects.filter(role='TEAM_MEMBER')
        self.fields['team_members'].required = False
        
