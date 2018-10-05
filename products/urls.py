
from django.contrib import admin
from django.urls import path
from .views import  productView,ProductDetailView,productlistview


urlpatterns = [
    path('',productlistview.as_view()),
    path('<slug:slug>/',ProductDetailView),
]

