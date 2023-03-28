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
    path(
        "contact_info/<str:business_id>/",
        create_business_contact_info,
        name="contact_info",
    ),
    path("medical_office/", medical_office_html, name="medical_office"),
    path("medical_office/medical_office/home/", homeView, name="home"),
    path("blog/", BlogPull, name="blog"),
    path(
        "view_business/<str:tempName>/<str:webId>/",
        view_user_business,
        name="view_business",
    ),
    # trying to see blog page template
    path("business/<int:business_id>/templates/", templatesView, name="templates"),
    # ------Drew's work on URLs for Bryan------#
    path("updatebusiness/<str:business_id>/", UpdateBusiness, name="update_business"),
    path(
        "updatebusinesscontactinfo/<str:business_id>/",
        UpdateBusinessContactInfo,
        name="update_contact_info",
    ),
    path("deletebusiness/<str:contact_id>/", DeleteBusiness, name="delete_business"),
    path(
        "deletebusinesscontactinfo/<str:contact_id>/",
        DeleteBusinessContactInfo,
        name="delete_business_contact_info",
    ),
    # --------End of Drew's work---------#
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
