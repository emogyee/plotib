from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile
from django.shortcuts import get_object_or_404


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user,channel_name=user.username)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})



def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')

def profile(request, username):
    user = get_object_or_404(User,username=username)
    profile, created = Profile.objects.get_or_create(user=user,defaults={'channel_name': user.username})

    return render(request,'profiles/profile.html',{'profile': profile})
@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')
def logout_user(request):
    logout(request)
    return redirect('login')
    
