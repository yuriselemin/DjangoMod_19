"""
URL configuration for DjangoMod_19 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from task1.views import games, main, cart, sign_up_by_html


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('store/', games, name='games'),
    path('cart/', cart, name='cart'),
    path('main/', main, name='main'),
    path('registration_page/', sign_up_by_html, name='sign_up_by_html'),
]