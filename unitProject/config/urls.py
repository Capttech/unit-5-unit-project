from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
<<<<<<< HEAD
    path("", home, name="home"),
    path("register/", RegisterPage, name="register"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("profile/", AccountSettings, name="profile"),
=======
    path("", root, name="root"),
    path("contact/", contact_view, name="contact"),
>>>>>>> parent of 9e76723 (I have 2 working login/ register views each)
]
