from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView

# from .forms import SignUpForm
from shop.forms import SignUpForm


class UserLoginView(LoginView):
    template = 'LoginView_form.html'

class UserSignupView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})