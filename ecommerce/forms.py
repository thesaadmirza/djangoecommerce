from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class ContactForm(forms.Form):
     name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
     email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control"}))
     message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))

     def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be Gmail")
        return email

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class RegisterForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))
    username= forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput())


    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is already taken")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is already taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("password not matched")
        return data

