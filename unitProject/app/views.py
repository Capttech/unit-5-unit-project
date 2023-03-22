from django.shortcuts import render
from app.forms import ContactForm, SignUpForm

# Create your views here.


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            context = {
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "message": message,
            }
            return render(request, "contact.html", context)
    else:
        form = ContactForm()
        return render(request, "contact.html")


def root(request):
    context = {}
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            context["signup_success"] = True
            form.save()
    else:
        form = SignUpForm()
    context["form"] = form

    return render(request, "root.html", context)
