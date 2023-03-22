from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", root, name="root"),
    path("contact/", contact_view, name="contact"),
]
