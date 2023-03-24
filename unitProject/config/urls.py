from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", RegisterPage, name="register"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("profile/", AccountSettings, name="profile"),
    # path("", homeView, name="home"),
    # path("templates/", templatesView, name="templates"),
    # path("businesses/", businessesView, name="businesses"),
    # path("profile/", profileView, name="profile"),
    # path("signup/", signupView, name="signup"),
    # path("login/", loginView, name="login"),
    # path("logout/", logoutView, name="logout"),
]
