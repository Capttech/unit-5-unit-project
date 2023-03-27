from django.shortcuts import render, redirect, get_object_or_404
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
from django.conf import settings
import os
from django.contrib import messages
from django.views.generic import DetailView
from django.http import HttpResponseNotFound
from django.contrib import messages
from django.template.loader import get_template, render_to_string

# the standard home view -Phillip
def homeView(request):
    return render(request, "home.html")


@unauthenticated_user
def RegisterPage(request):
    context = {}
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
                user_name=user.username,
                user_email=user.email,
            )
            login(request, user)
            messages.success(request, "Account was created for " + username)
            return redirect("home")
        else:
            errors = form.errors.as_data()
            error_messages = {}
            for field, error_list in errors.items():
                error_messages[field] = [error.message for error in error_list]
                context = {"form": form, "error_messages": error_messages}

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
                messages.success(request, "{{username}} has been created")
                login(request, user)
                return redirect("home")

            else:
                messages.info(request, "Username OR Password is Incorrect")

    context = {"form": form}
    return render(request, "login.html", context)


def LogoutUser(request):
    logout(request)
    return redirect("home")


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


def businessesView(request):
    businesses = businessTemplateDatabase.objects.all()
    business_contact = businessContactInfoDatabase.objects.filter(
        business__in=businesses
    )
    context = {"businesses": businesses, "business_contact": business_contact}
    return render(request, "template.html", context)


@login_required(login_url="login")
def create_business(request):
    profile = request.user.profile
    templateId = generateUserId()
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.templateId = generateWebsite(templateId, profile)
            business.profile = request.user.profile
            business.save()
            return redirect("businesses")
    else:
        form = BusinessForm()

    context = {"form": form}
    return render(request, "create_business.html", context)


@login_required(login_url="login")
def create_business_contact_info(request, business_id):
    businesses = businessTemplateDatabase.objects.filter(name=request.user.profile.user)
    business = businessTemplateDatabase.objects.get(id=business_id)
    if request.method == "POST":
        form = BusinessContactInfoForm(request.POST)
        if form.is_valid():
            contact_info = form.save(commit=False)
            contact_info.business = business
            contact_info.save()

            return redirect("businesses")

    else:
        form = BusinessContactInfoForm()
    return render(request, "contact_info.html", {"form": form, "business": business})


def templatesView(request, business_id):
    try:
        business = businessTemplateDatabase.objects.get(id=business_id)
    except businessTemplateDatabase.DoesNotExist:
        return HttpResponseNotFound("Business does not exist")

    template_choice = business.template_choice

    if template_choice == "medical_office":
        context = {"medical_office": "This is data for Template 1"}
        return render(request, "medical_office.html", context)
    elif template_choice == "Blog":
        context = {"Blog": "This is data for Template 2"}
        return render(request, "Nav_bar.html", context)
    else:
        context = {"Phillip": "This is data for Template 3"}
        return render(request, "template_3.html", context)


# ====everything above this line works==========#


#
allTemplates = {}
allTemplates["drew"] = "medical_office"
allTemplates["jarvis"] = "blog"


@login_required(login_url="login")
def view_user_business(request, tempName, webId):
    if not tempName:
        # if tempName is empty, return a 404 error response
        return HttpResponseNotFound()
    else:
        allGeneratedSites = generatedWebsites.objects.all()
        allCreatedTemplates = businessTemplateDatabase.objects.all()
        foundTemplateId = ""
        foundTemplateData = []

        for site in allGeneratedSites:
            if site.webId == webId:
                foundTemplateId = site.templateId

        for template in allCreatedTemplates:
            if template.id == foundTemplateId:
                foundTemplateData = template

        if foundTemplateId == "":
            return render(f"{allTemplates[tempName]}.html")
        else:
            return render(f"{allTemplates[tempName]}.html", foundTemplateData)


# test to see blog
def BlogPull(request):
    return render(request, "Nav_bar.html")


# -----Drew's work-----#
@login_required(login_url="login")
def medical_office_html(request):
    return render(request, "medical_office.html")


# ------End of Drew's work-------#
