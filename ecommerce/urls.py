"""ecommerce URL Configuration

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
from django.conf.urls.static import static
from .views import homePage,contactPage,aboutPage,LoginPage,RegisterPage
from products.views import  productView,ProductDetailView,productlistview
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage),
    path('login/',LoginPage),
    path('register/',RegisterPage),
    path('contactPage/',contactPage),
    path('aboutPage/',aboutPage),
    path('list',productlistview.as_view()),
    path('product/<int:id>/',ProductDetailView),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)