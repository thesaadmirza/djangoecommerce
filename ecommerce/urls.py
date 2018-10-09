
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from .views import homePage,contactPage,aboutPage,LoginPage,RegisterPage
from products.views import  productView,ProductDetailView,productlistview
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',homePage,name='home'),
    path('login/',LoginPage,name='login'),
    path('register/',RegisterPage,name='register'),
    path('contactPage/',contactPage,name='contact'),
    path('aboutPage/',aboutPage,name='about'),
    path('products/',include(('products.urls','products'),namespace='products')),
    path('search/',include(('search.urls','search'),namespace='search')),
   
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)