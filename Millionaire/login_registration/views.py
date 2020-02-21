from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def index(request):
    """Home page."""
    return render(request, 'login_registration/index.html')


@login_required
def user_logout(request):
    """Logout the user."""
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    """Register new user."""
    registered = False
    user = None
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'login_registration/registration.html',
                  {'user': user,
                   'user_form': user_form,
                   'registered': registered})


def user_login(request):
    """Login with existing credentials."""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print(f"They used username: {username} and password: {password}")
            messages.error(request, 'Wrong username or password')
            return render(request, 'login_registration/login.html')
    else:
        return render(request, 'login_registration/login.html')
