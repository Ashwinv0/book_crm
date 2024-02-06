from django import forms
from work.models import Book
from work.models import Students

class EmpForm(forms.Form):
    name=forms.CharField()
    place=forms.CharField()
    salary=forms.CharField()
    contact=forms.CharField()

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields=['title','genre','author']

class StudentsForm(forms.ModelForm):
    class meta:
        model = Students
        fields =['name','age','course','gender','place']

