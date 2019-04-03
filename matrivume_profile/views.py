from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from matrivume_profile.forms import LoginForm, IdentityForm
from matrivume_profile import models
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
            user = User.objects.create_user(username=username, password=password)
            identity = models.Identity.objects.create(user_profile=user)
            identity.save()

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


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('matrivume_profile:login'))


@login_required()
def profile_view(request):
    profile_model = models.Identity.objects.filter(user_profile=request.user).first()
    context = {
        'profile': profile_model
    }
    return render(request, 'matrivume_profile/profile.html', context=context)


@login_required()
def profile_update_view(request):
    profile_model = models.Identity.objects.filter(user_profile=request.user).first()
    if request.method == 'POST':
        form = IdentityForm(data=request.POST)

        if form.is_valid():
            birth_date = form.cleaned_data['birth_date']
            github_profile_link = form.cleaned_data['github_profile_link']
            bio = form.cleaned_data['bio']
            profile_model.birth_date = birth_date
            profile_model.github_profile_link = github_profile_link
            profile_model.bio = bio
            profile_model.save()
            return HttpResponseRedirect(reverse('matrivume_profile:profile_view'))

    form = IdentityForm(initial={
        'birth_date': profile_model.birth_date,
        'github_profile_link': profile_model.github_profile_link,
        'bio': profile_model.bio
    })
    context = {
        'form': form,
        'profile': profile_model
    }
    return render(request, 'matrivume_profile/profile.html', context=context)
