"""Ecomm_App URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
# from .views import *
from .import views
urlpatterns = [
    path('show/',views.show),
    path('button/',views.button),
    path('login/',views.login),
    path('typography/',views.typography),
    path('element/',views.element),
    path('signup/',views.usersignup),
    path('dashboard/', views.Dashboard),
    path('usersignup/',views.UserSignupAPI.as_view(), name='UserSignupAPI'),
    path('userlogin/',views.userLoginAPI.as_view(),name='userLoginAPI'),
    path('myprofile/',views.MyProfileAPI.as_view(),name='MyProfileAPI'),
    path('maincategory/',views.MainCategoryAPI.as_view(),name='MainCategoryAPI'),
    path('subcategory/',views.SubCategoryAPI.as_view(),name = 'SubCategoryAPI'),
    # path('product/',views.)
]
