from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", RegisterPage, name="register"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("edit_profile/", AccountSettings, name="edit_profile"),
]
