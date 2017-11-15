from django import forms
from django.contrib.auth import login,logout,authenticate,get_user_model

User = get_user_model()

class UsersInfo(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Username or Password does not match")

        return super(UsersInfo,self).clean(*args,**kwargs)


class RegisterForm(forms.ModelForm):
    email = forms.EmailField()
    confirm_email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'confirm_email',
            'password',
            'confirm_password',

        ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        check_username = User.objects.filter(username=username)

        if check_username.exists():
            raise forms.ValidationError("Username Already in Use")

        return username

    def clean_confirm_email(self):
        confirm_email = self.cleaned_data.get('confirm_email')
        email = self.cleaned_data.get('email')


        if email != confirm_email:
            raise forms.ValidationError("Emails Do Not Match")

        check_email = User.objects.filter(email=email)
        if check_email.exists():
            raise forms.ValidationError("Email Already in Use")

        return email

    def clean_confirm_password(self):
        confirm_password = self.cleaned_data.get('confirm_password')
        password = self.cleaned_data.get('password')


        if password != confirm_password:
            raise forms.ValidationError("Passwords Do Not Match")

        return password