from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from matrivume_profile.forms import LoginForm
# Create your views here.

User = get_user_model()


def user_registration_view(request):
    if request.method == 'POST':
        print("Just doing")
        form = UserCreationForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            User.objects.create_user(username=username, password=password)

            return HttpResponseRedirect(reverse('matrivume_profile:login'))

    form = UserCreationForm()
    return render(request, "matrivume_profile/registration.html", {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user=user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()
    return render(request, "matrivume_profile/login.html", {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('matrivume_profile:login'))
