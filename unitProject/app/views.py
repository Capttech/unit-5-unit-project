from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import *
from django.contrib.auth.forms import AuthenticationForm
from .manager import *
import os
from django.conf import settings
from django.contrib import messages
from django.views.generic import DetailView


@login_required(login_url="login")
def home(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "index.html", context)


@unauthenticated_user
def RegisterPage(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")

            group = Group.objects.get(name="profile")
            user.groups.add(group)
            Profile.objects.create(
                user=user,
                name=user.username,
                email=user.email,
            )
            login(request, user)
            messages.success(request, "Account was created for " + username)
            return redirect("home")
        else:
            # Add error messages to the form fields with errors
            for field, errors in form.errors.items():
                messages.error(
                    request, f"{field}: {', '.join(errors)}", extra_tags="danger"
                )

    context = {"form": form}
    return render(request, "register.html", context)


@unauthenticated_user
def LoginPage(request):
    form = AuthenticationForm()

    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Username OR Password is Incorrect")

    context = {"form": form}
    return render(request, "login.html", context)


def LogoutUser(request):
    logout(request)
    return redirect("login")


from django.conf import settings
import os


@login_required(login_url="login")
def AccountSettings(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            if "profile_pic" in request.FILES:
                profile.profile_pic = request.FILES["profile_pic"]
            profile.save()
            form.save()

    context = {"form": form}
    return render(request, "edit_profile.html", context)


# the standard home view -Phillip
def homeView(request):
    return render(request, "home.html")


def templatesView(request):
    ...


def businessesView(request):
    ...


def profileView(request):
    ...


class WebsiteDetailView(DetailView):
    model = generatedWebsites
    template_name = "website_detail.html"
