"""eSports URL Configuration

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
from django.urls import path, include
from users import views as user_views
from registration.backends.simple.views import RegistrationView
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static


class MyRegistrationView(RegistrationView):
    def get_success_url(self, user):
        return reverse('register_profile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contest.urls')),
    path('accounts/register/',
         MyRegistrationView.as_view(),
         name='registration_register'),
    path('accounts/', include('registration.backends.simple.urls')),
    path('register_profile/', user_views.register_profile, name='register_profile'),
]
