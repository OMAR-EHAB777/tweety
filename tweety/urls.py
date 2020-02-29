"""tweety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include , re_path
from django_registration.backends.one_step.views import RegistrationView
from accounts.forms import CustomUserForm
from core.views import IndexTemplateView
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='documentationAPI')
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'document/', schema_view),
    #custom verfitionform provide by django  registrationview
    path("accounts/register/",
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/",
             ), name="django_registration_register"),
    #django registration packge urls
    path("accounts/",
         include("django_registration.backends.one_step.urls")),
    #login-path
    path("accounts/",
         include("django.contrib.auth.urls")),
    #api-login-accounts
    path("api/",
         include("accounts.api.urls")),
    #api-tweets-urls
    path("api/",
         include("tweets.api.urls")),
    #login api
    path("api-auth/",
         include("rest_framework.urls")),
    #login-rest/endpoints
    path("api/rest-auth/",
         include("rest_auth.urls")),
    #registration-rest/endpoint
    path("api/rest-auth/registration/",
         include("rest_auth.registration.urls")),
    re_path(r"^.*$", IndexTemplateView.as_view(), name="entry-point")
]
