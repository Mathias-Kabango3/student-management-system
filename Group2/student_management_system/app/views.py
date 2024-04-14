from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student,Grade,Module
from .forms import StudentForm
  
# Create your views here.
def index(request):
  return render(request, 'index.html', {
    'students': Student.objects.all()
  })


def view_student(request, id):
  return HttpResponseRedirect(reverse('index'))

# @login_required(login_url='login')
def add(request):
  print(request.user)
  if request.method == 'POST' and request.user.is_superuser:
    form = StudentForm(request.POST)
    if form.is_valid():
      new_student_number = form.cleaned_data['student_number']
      new_first_name = form.cleaned_data['first_name']
      new_last_name = form.cleaned_data['last_name']
      new_email = form.cleaned_data['email']
      new_field_of_study = form.cleaned_data['field_of_study']
      

      new_student = Student(
        student_number=new_student_number,
        first_name=new_first_name,
        last_name=new_last_name,
        email=new_email,
        field_of_study=new_field_of_study,
      )
      new_student.save()
      return render(request, 'add.html', {
        'form': StudentForm(),
        'success': True
      })
  else:
    form = StudentForm()
  return render(request, 'add.html', {
    'form': StudentForm()
  })

# @login_required(login_url='login')
def update(request, id):
  if request.method == 'POST' and request.user.is_superuser:
    student = Student.objects.get(pk=id)
    form = StudentForm(request.POST, instance=student)
    if form.is_valid():
      form.save()
      return render(request, 'edit.html', {
        'form': form,
        'success': True
      })
  else:
    student = Student.objects.get(pk=id)
    form = StudentForm(instance=student)
  return render(request, 'edit.html', {
    'form': form
  })

# @login_required(login_url='login')
def delete(request, id):
  if request.method == 'POST'and request.user.is_superuser:
    student = Student.objects.get(pk=id)
    student.delete()
  return HttpResponseRedirect(reverse('index'))

def login(request):
    if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = User.objects.get(username=username)
      user  = authenticate(request,username=username,password=password)
      if user:
        return redirect('index')
    return render(request,'login.html')

def details(request,pk):
  username = Student.objects.get(pk=pk).student_number
  grades = Grade.objects.filter(student=username)
  student = Student.objects.get(pk=pk)
  return render(request,'details.html',{'grades':grades,'student':student})




   

