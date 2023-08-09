from django import forms
from.models import  UserAccount

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserAccount
        fields = ['username','password','name','age','gender','phone_number','address','dob','mail_id','account_type','district','branch','materials']
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
