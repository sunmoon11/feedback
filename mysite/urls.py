"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
import sendmail.views
import api.views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/login', csrf_exempt(api.views.login)),
    url(r'^api/register', csrf_exempt(api.views.register)),

    url(r'^signin', auth_views.login, {'template_name': 'signin.html'}, name='page_signin'),
    url(r'^signup', sendmail.views.signup, {'template_name': 'signup.html'}, name='page_signup'),
    url(r'^sendmail', sendmail.views.sendmail, name='page_sendmail'),
    url(r'^$', sendmail.views.home, name='page_home'),
]
