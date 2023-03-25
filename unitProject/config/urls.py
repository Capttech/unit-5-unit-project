from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", RegisterPage, name="register"),
    path("login/", LoginPage, name="login"),
    path("logout/", LogoutUser, name="logout"),
    path("edit_profile/", AccountSettings, name="edit_profile"),
    path("", homeView, name="home"),
    path("add_business/", create_business, name="add_business"),
    path("businesses/", businessesView, name="businesses"),
    path("profile/", profileView, name="profile"),
    path("medical_office/", medical_office_html, name="medical_office"),
    path("medical_office/medical_office/home/", homeView, name="home"),
    path("blog/", BlogPull, name="blog"),
    path(
        "view_business/<str:tempName>/<str:webId>/",
        view_user_business,
        name="view_business",
    ),
    # ================|bryan's work|=======================#
    # path("template/new/", create_template, name="template_create"),
    # path("template/<int:pk>/", create_template, name="template_detail"),
    # path("submission/new/", form_submission, name="form_submission"),
    # path("submission/<int:pk>/", form_submission, name="submission_detail"),
    # path("generate/<int:submission_id>/", generate_html, name="generate_html"),
    # path(
    #     "submissions/<int:submission_id>/edit/", edit_submission, name="edit_submission"
    # ),
    # path(
    #     "submissions/<int:submission_id>/delete/",
    #     delete_submission,
    #     name="delete_submission",
    # ),
    # path(
    #     "submissions/<int:submission_id>/upload_image/",
    #     upload_image,
    #     name="upload_image",
    # ),
    # path(
    #     "submissions/<int:submission_id>/", submission_detail, name="submission_detail"
    # ),
    # trying to see blog page template
    path("templates/", templatesView, name="templates"),
    # path("businesses/", businessesView, name="businesses"),
    # path("profile/", profileView, name="profile"),
    # path("signup/", signupView, name="signup"),
    # path("login/", loginView, name="login"),
    # path("logout/", logoutView, name="logout"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
