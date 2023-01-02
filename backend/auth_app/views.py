from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from auth_app.forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    
    return render(request, 'home.html')

def registerpage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data['username']
            messages.success(request,'Account Created Successfully for' +user)
            return redirect('loginpage')

    return render(request, 'registerPage.html', {'form':form})

def loginpage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('individualreport')
        else:
            messages.info(request,'Username or Password is incorrect')
            return redirect('loginpage')


    return render(request, 'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect('loginpage')

@login_required(login_url='login')
def individualreport(request):
    return render(request, 'individualreport.html')