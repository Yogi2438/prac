from django import forms
from .models import student
class regform(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'palceholder':'Enter Password'}),max_length=10)
	class Meta:
		model = student
		fields = ['name','std','roll_no','password']

class loginform(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput(attrs={'palceholder':'Enter Password'}),max_length=10)
	class Meta:
		model = student
		fields = ['name','password']
	
# demo 
# password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'masseges','palceholder':'Enter Password'}),requierd=True,max_length=10)
	
