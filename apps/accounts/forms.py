from django import forms
from .models import CustomUser,Profile
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['username','email','role','password1','password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in ['username','email','role','password1','password2']:
            self.fields[field].help_text = None

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'autofocus':True})
    )
    password = forms.CharField(
        label='Password',
        strip=False,
        widget=forms.PasswordInput()
    )

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','fname','lname','contact']
        widgets = {
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['avatar'].help_text = None  # Remove help text
        self.fields['avatar'].widget.clear_checkbox_label = ''  # Remove "Clear" checkbox label
        self.fields['avatar'].widget.initial_text = ''