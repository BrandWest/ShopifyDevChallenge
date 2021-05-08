from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

#Custome Views
from shop.forms import UserProfile, ImageForm
from shop.models import Images, PostImage

#Access Homepage
class HomePageView(ListView):
    model = Images
    template_name = 'home.html'

class UserLoginView(LoginView):
    template = 'LoginView_form.html'

class UserSignupView(CreateView):
    form_class = UserProfile
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

def ImageRepoView(request):
    image = Images.objects.all()
    return render(request, 'image_repo.html', {'image' : image})


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
        form = UserProfile(request.POST)
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
        form = UserProfile()
    return render(request, 'signup.html', {'form': form})

#User upload view
def ImageUploadView(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save(commit=False)
            form.current_user = request.user
            print(request.user)
            form.save()
            image_object = form.instance
            return render(request,"image_repo.html", {"image_object":image_object, "current_user":request.user})
    else:
        form=ImageForm()
    all_images=Images.objects.all()
    return render(request, "image_repo.html", {"all_images":all_images, "form":form,  "current_user":request.user})

