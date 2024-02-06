from django.shortcuts import redirect, render
from django.views.generic import View
from work.forms import EmpForm,BookForm,StudentsForm
from work.models import Emp,Book,Students


# Create your views here.

class Employe(View):
    def get(self,request):
        form=EmpForm()
        return render(request,"add.html",{"form":form})

    def post(self,request):
        form=EmpForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Emp.objects.create(**form.cleaned_data)

            return render(request,"add.html",{"form":form})
        else:
            return render(request,"add.html",{"form":form})



class BookView(View):
    def get(self,request):
        form=BookForm()
        return render(request,"book.html",{"form":form})
    
    def post(self,request):
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()

            # form.save():method to add the data into database without using orm query(only for modelforms)
            # Book.objects.create(**form.cleaned_data)  === ORM QUERY

            print("created")
            return render(request,"book.html",{"form":form})
        else:
            return render(request,"book.html",{"form":form})

class Booklist(View):
    def get(self,request):
        qs = Book.objects.all()
        return render(request,"booklist.html",{"qs":qs})

class Book_DetailView(View):

    def get(self,request,*args,**kwargs):
        # (**kwargs) provides with flexibility to use keyword arguments
        # in our program.Using it as a parameter we can eventually pass
        # many arguments(requests)
        print(kwargs)
        id=kwargs.get("pk")
        
        qs=Book.objects.get(id=id)
        return render(request,"bookd.html",{"data":qs})

class Book_Delete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Book.objects.get(id=id).delete()
        return redirect("book-al")








class StudentsView(View):
    def get(self,request):
        form=StudentsForm()
        return render(request,"student.html",{"form":form})
    
    def post(self,request):
        form=StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            print("created")
            return render(request,"student.html",{"form":form})
        else:
            return render(request,"student.html",{"form":form})
        

