from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required

#Custome Views
from shop.forms import UserProfile, ImageForm
from shop.models import Images

#Class Access Homepage
class HomePageView(ListView):
    model = Images
    template_name = 'home.html'

#Class User login
class UserLoginView(LoginView):
    template = 'LoginView_form.html'

#Class User signup
class UserSignupView(CreateView):
    form_class = UserProfile
    success_url = reverse_lazy('login')
    template_name = 'commons/signup.html'

#Image repo view, login required
@login_required
def ImageRepoView(request):
    form=ImageForm(request.POST or None, request.FILES or None)
    all_images = Images.objects.all()
    return render(request, 'image_repo.html', {'all_images' : all_images})

#User login attempt
def login_attempt(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('image_repo')
    else:
        return redirect('home')

#User logout view
def logout_view(request):
    logout(request)

#user signup
def signup(request):
    if request.method == 'POST':
        form = UserProfile(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserProfile()
    return render(request, 'signup.html', {'form': form})

# User upload view
@login_required
def ImageUploadView(request):
    if request.method == "POST":
        form=ImageForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            user = request.user
            image = form.cleaned_data['images']
            caption = form.cleaned_data['caption']
            for file in files:
                Images.objects.create(current_user=user, images=image, caption=caption)
            return render(request, "image_repo.html")
        else:
            all_images = Images.objects.all()
            return render(request, "image_repo.html", {"all_images": all_images, "form": form, "current_user": request.user})
    else:
        form=ImageForm()
        all_images = Images.objects.all()
        return render(request, "image_repo.html", {"all_images": all_images, "form": form, "current_user": request.user})

@login_required
def ImageDeletionView(request, pk):
    try:
        imageID = Images.objects.get(id=int(pk))
        print("image iD: " + str(imageID))
        print("pk: " + str(pk))
    except Images.DoesNotExist:
        print("failed Does not exist")
        return redirect(request, "image_repo.html")

    if request.method == 'POST':
        if request.user != Images.get_username(imageID):
            print( "User != User" )
            all_images = Images.objects.all()
            return HttpResponse(render(request, "image_repo.html", {"all_images": all_images}))
        else:
            print( "User = User" )
            Images.objects.filter(id=pk).delete()
    else:
        all_images = Images.objects.all()
        return HttpResponse(render(request, "image_repo.html", {"all_images": all_images}))
    all_images = Images.objects.all()
    return HttpResponse(render(request, "image_repo.html", {"all_images": all_images}))