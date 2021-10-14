from .models import Student
from django.shortcuts import render,redirect
from .forms import StudentRegistrationForm
from .models import Student
from django.http import HttpResponse

# Create your views here.Views are simple functions in python that take in user requests for certiain pages or recources on my site and then in the views we define what result the user should get for their request
def index(request):
    return render(request,' index.html',{})#return = result the user should see, indexx=specify which template should be seen,the empty dictionary you can pass info you want to be injected into the html

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student:student_list')
        else:
            print(form.errors)    
    else:
        form = StudentRegistrationForm()
    return render(request,'register_student.html',{'form':form})

def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'students':students})

def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=='POST':
        form=StudentRegistrationForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
        return redirect('student:student_list')    
    else:
        form=StudentRegistrationForm(instance=student)
        return render(request,'edit_student.html',{'form':form})        
        
def student_profile(request,id):
    student=Student.objects.get(id=id)
    return render(request,'student_profile.html',{'student':student})

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('student:student_list')

# Create your views here.
