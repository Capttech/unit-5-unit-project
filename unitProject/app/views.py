from app.forms import ContactForm, SignUpForm
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


def ContactPage(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            form.save()
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "message": message,
            }
            return render(request, "contact.html", context)
    else:
        form = ContactForm()

    context = {"form": form}
    return render(request, "contact.html", context)


def home(request):
    users = User.objects.all()
    contacts = Contact.objects.all()
    context = {"users": users, "contacts": contacts}
    return render(request, "index.html", context)


def root(request):
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            context["signup_success"] = True
            form.save()
    else:
        form = SignUpForm()
    context = {"form": form}

    return render(request, "root.html", context)


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

            messages.success(request, "Account was created for " + username)
            return redirect("login")

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


@login_required(login_url="login")
def ProfilePage(request, pk):
    