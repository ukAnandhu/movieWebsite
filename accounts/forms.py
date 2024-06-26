from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from accounts.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password',
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter Password'

    }))

    class Meta:
        model = CustomUser 
        fields = ['username','first_name','last_name','email','password']

    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Enter Firstname'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Lastname'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
            
    def clean(self):
        cleaned_data = super(CustomUserCreationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
                'Password Does not match!'
            )


class CustomAuthenticationForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password']
    def __init__(self,*args,**kwargs):
        super(CustomAuthenticationForm,self).__init__(*args,**kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter email id'
        self.fields['password'].widget.attrs['placeholder'] = 'Enter password'

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'