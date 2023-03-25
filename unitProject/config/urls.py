from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("register/", RegisterPage, name="register"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("edit_profile/", AccountSettings, name="edit_profile"),
    path("", homeView, name="home"),
    path("templates/", templatesView, name="templates"),
    path("businesses/", businessesView, name="businesses"),
    path("profile/", profileView, name="profile"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
