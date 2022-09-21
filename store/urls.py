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
    path('widget/',views.widget),
    path('form/',views.form),
    path('chart/',views.chart),
    path('error/',views.error),
    path('forgotpassword/',views.forgotpassword),
    path('blank/',views.blank),
    path('usersignup/',views.UserSignupAPI.as_view(), name='UserSignupAPI'),
    path('userlogin/',views.userLoginAPI.as_view(),name='userLoginAPI'),
    path('myprofile/',views.MyProfileAPI.as_view(),name='MyProfileAPI'),
    path('maincategory/',views.MainCategoryAPI.as_view(),name='MainCategoryAPI'),
    path('subcategory/',views.SubCategoryAPI.as_view(),name = 'SubCategoryAPI'),
    path('ProductAPI/',views.ProductAPI.as_view(),name = 'ProductAPI'),
    path('OfferAPI/',views.OfferAPI.as_view(),name='OfferAPI'),
    path('DiscountAPI/',views.DiscountAPI.as_view(),name='DiscountAPI'),
    path('signupp/',views.signup),
    path('hello/', views.HelloView.as_view(), name ='hello'),
    path('AddToWishlistAPI/', views.AddToWishlistAPI.as_view(), name ='AddToWishlistAPI'),
    path('AddToCartAPI/', views.AddToCartAPI.as_view(), name ='AddToCartAPI'),
    path('WishlistAPI/', views.WishlistAPI.as_view(), name ='WishlistAPI'),
    path('FilterByNameAPI/', views.FilterByNameAPI.as_view(), name ='FilterByNameAPI'),
    path('SizeAPI/', views.SizeAPI.as_view(), name ='SizeAPI'),
    path('ColorAPI/', views.ColorAPI.as_view(), name ='ColorAPI'),
    path('GenderAPI/', views.GenderAPI.as_view(), name ='GenderAPI'),
    path('BrandAPI/', views.BrandAPI.as_view(), name ='BrandAPI'),
    path('ProductListAPI/', views.ProductListAPI.as_view(), name ='ProductListAPI'),
    path('StaffAPI/', views.StaffAPI.as_view(), name ='StaffAPI'),
    path('HotelAPI/', views.HotelAPI.as_view(), name ='HotelAPI'),
    path('image_request/', views.image_request, name = "image-request")  
]
