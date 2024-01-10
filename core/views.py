from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm, LoginForm

# Create your views here.


def homepage(request):
    # """The view for the main page of the site."""
    # Render an HTML template - this is where you should put most of your code.
    return render(request, 'core/index.html')


def register(request):
    form = CreateUserForm()
    if request.method == "POST":  # If the form has been submitted...
        form = CreateUserForm(request.POST)  # A form bound to the POST data
        if form.is_valid():  # All validation rules pass
            form.save()  # Save the new user
            return redirect('my-login')
        
    context = {'form': form}
    return render(request, 'core/register.html', context=context)


def my_login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
            
    
    context = {'form': form}
    return render(request, 'core/my-login.html', context=context)


    


@login_required(login_url='my-login')
def dashboard(request):

    return render(request, 'core/dashboard.html')




    


def user_logout(request):
    auth.logout(request)
    return redirect('')
