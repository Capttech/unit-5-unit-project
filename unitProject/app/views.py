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
import os
from django.conf import settings
from django.contrib import messages
from django.views.generic import DetailView


# @login_required(login_url="login")
# def home(request):
#     users = User.objects.all()
#     context = {"users": users}
#     return render(request, "index.html", context)


from django.contrib import messages


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


@login_required
def businessesView(request):
    businesses = businessTemplateDatabase.objects.all()
    return render(request, "template.html", {"businesses": businesses})
    submissions = Submission.objects.filter(profile=request.user.profile)
    return render(request, "submission_list.html", {"submissions": submissions})


def profileView(request):
    ...


# ====| what bryan is working on below |=========
class WebsiteDetailView(DetailView):
    model = generatedWebsites
    template_name = "website_detail.html"


from django.shortcuts import render, redirect
from .models import Template, Submission


# @login_required
def form_submission(request):
    if request.method == "POST":
        # Get data from the form
        template_id = request.POST.get("template_id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        # Create a new submission instance with the data
        submission = Submission.objects.create(
            template_id=template_id, name=name, email=email, message=message
        )
        # Generate the HTML page using the selected template and the submission data
        template = Template.objects.get(id=template_id)
        context = {"submission": submission}
        html = template.render(context)
        # Save the HTML page to the database
        submission.html = html
        submission.save()
        # Redirect the user to the new HTML page
        return redirect("submission_detail.html", pk=submission.pk)
    else:
        # If the request method is not POST, render the form template
        templates = Template.objects.all()
        context = {"templates": templates}
        return render(request, "form.html", context)


@login_required
def create_template(request):
    if request.method == "POST":
        # Create a new Template object with the submitted data
        template = Template(
            name=request.POST["name"],
            description=request.POST["description"],
            content=request.POST["content"],
            owner=request.user.profile,
        )
        template.save()
        return redirect("template_detail.html", pk=template.pk)
    else:
        # Render a form for the user to create a new template
        return render(request, "create_template.html")


@login_required
def generate_html(request, submission_id):
    # Retrieve the submission object
    submission = get_object_or_404(Submission, pk=submission_id)

    # Retrieve the template object
    template = submission.template

    # Define the context to render the template with
    context = {
        "submission": submission,
        "template": template,
    }

    # Render the HTML template with the context
    return render(request, template.html_file.name, context)


# -----Drew's work-----#
@login_required
def medical_office_html(request):
    if request.method == "POST":
        template = Template(
            name=request.POST["name"],
            description=request.POST["description"],
            content=request.POST["content"],
            owner=request.user.profile,
        )
        template.save()
        return redirect("medical_office.html", pk=template.pk)
    else:
        return render(request, "home.html")


# ------End of Drew's work-------#


@login_required
def create_business(request):
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            business = form.save(commit=False)
            business.save()
            return redirect("generate_template.html", pk=business.pk)
    else:
        form = BusinessForm()

    context = {"form": form}
    return render(request, "create_business.html", context)


# views.py


@login_required
def edit_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if request.method == "POST":
        form = SubmissionForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            return redirect("submission_detail.html", submission_id=submission_id)
    else:
        form = SubmissionForm(instance=submission)
    return render(request, "edit_submission.html", {"form": form})


@login_required
def delete_submission(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    submission.delete()
    return redirect("submission_list.html")


@login_required
def upload_image(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    if request.method == "POST":
        image = request.FILES["image"]
        submission.image.save(image.name, image)
        submission.save()
        return redirect("submission_detail.html", submission_id=submission_id)
    return render(request, "upload_image.html", {"submission": submission})


@login_required
def submission_detail(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    return render(request, "submission_detail.html", {"submission": submission})


@login_required
def submission_list(request):
    submissions = Submission.objects.filter(profile=request.user.profile)
    return render(request, "submission_list.html", {"submissions": submissions})


# =====| end of bryan work===================#

# test to see blog
def BlogPull(request):
    return render(request, "Nav_bar.html")
