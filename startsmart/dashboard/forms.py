from cProfile import label
from django import forms
from . models import *
from django.contrib.auth.forms import UserCreationForm

class NotesForm(forms.ModelForm):
    class Meta:
        # Mapping model class note section
        model= Notes 
        fields = ['title', 'description']

class DateInput(forms.DateInput):
    input_type= 'date'

class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework                                   #redirects to models.py class homework
        widgets = {'due': DateInput()}    
                     #Widget is an element of Graphical User Interface (GUI) that displays/illustrates information or gives a way for the user to interact with the OS.                 
        fields = ['subject', 'title', 'description', 'due', 'is_finished']



            #common class for youtube, books, dictionary search
class DashboardFom(forms.Form):
    text = forms.CharField(max_length=100 , label="Search here :")

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo 
        fields = ['title', 'is_finished']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username', 'password1','password2']