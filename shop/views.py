from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView

class UserLoginView(LoginView):
    template = 'LoginView_form.html'


def login_attempt(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return

    else:
        return
def logout_view(request):
    logout(request)