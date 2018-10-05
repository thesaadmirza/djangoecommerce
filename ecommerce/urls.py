
from django.contrib import admin
from django.urls import path,include
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
    path('products/',include('products.urls')),
   
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)