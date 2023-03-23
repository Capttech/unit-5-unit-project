from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import *


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("home")
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# def allowed_users(allowed_roles=[]):
#     def decorator(view_func):
#         def wrapper_func(request, *args, **kwargs):

#             group = None
#             if request.user.groups.exists():
#                 group = request.user.groups.all()[0].name

#             if group in allowed_roles:
#                 return view_func(request, *args, **kwargs)

#             else:
#                 return HttpResponseForbidden()

#         return wrapper_func

#     return decorator


# def admin_only(view_func):
#     def wrapper_function(request, *args, **kwargs):
#         group = None
#         if request.user.groups.exists():
#             group = request.user.groups.all()[0].name

#         if group == "profile":
#             return redirect("home")

#         if group == "admin":
#             return view_func(request, *args, **kwargs)

#         return HttpResponseForbidden()

#     return wrapper_function


# def user_is_customer(view_func):
#     def wrapper(request, pk, *args, **kwargs):
#         print("pk:", pk)
#         customer = get_object_or_404(Customer, id=pk)
#         print("customer:", customer)
#         print("user:", request.user)  # add this line
#         if request.user.is_staff or request.user.customer.id == pk:
#             return view_func(request, pk, *args, **kwargs)
#         else:
#             return redirect("login")

#     return wrapper


# customer_login_required = user_passes_test(
#     lambda u: u.is_authenticated and not u.is_staff, login_url="login"
# )
