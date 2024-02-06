from django.shortcuts import render
from django.views.generic import View
from operation.forms import Formname

class FormView(View):
    def get(self,request):
        form = Formname
        return render(request,"form.html",{"form":form})
    
    def post(self,request):
        print(request.POST)
        form = Formname(request.POST)
        if form.is_valid():
            print("name",form.cleaned_data["name"])
            print("email",form.cleaned_data["email"])
        else:
            print("gud by")

        return render(request,"form.html",{"form":form})



# Create your views here.

# function based views(fbv)
# class based views(Cbv)

class HelloworldView(View):
    def get(self,request):
        return render(request,"Helloworld.html")
    
class HelloView(View):
    def get(self,request):
        return render(request,"Hello.html")
    
class AddView(View):
    def get(self,request):
        return render(request,"Add.html")
    
    def post(self,request):
        print(request.POST)
        request.POST.get("num1")
        request.POST.get("num2")

        n1= int(request.POST["num1"])
        n2= int(request.POST["num2"])
        result= n1+n2
        print(result)
        return render(request,"add.html",{"res":result})
        
class NumberView(View):
    def get(self,request):
        return render(request,"num.html")
    
    def post(self,request):
        request.POST.get("number")
        num= int(request.POST.get("number"))
        if num%2 == 0:
            res="even"
        else:
            res="odd"
        return render(request,"num.html",{"result":res})
    
class GreetView(View):
    def get(self,request):
        return render(request,"greet.html")
    
    def post(self,request):
        request.POST.get("name")
        name=request.POST.get("name")
        greetings="hello "+name+"!"
        return render(request,"greet.html",{"res":greetings})