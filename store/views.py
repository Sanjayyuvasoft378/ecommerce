from pickle import FALSE
from shutil import ExecError
from traceback import print_tb
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,authenticate,logout
from urllib.parse import uses_relative
from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.http import JsonResponse
from django.conf import settings
from django.core.mail import send_mail
# from store.models import Offer, Product, SubCategory, User, mainCategory
from .models import *
# from store.serializers import MainCategorySerializer, OfferSerializer, ProductSerializer, SubCategorySerializer, UserSerializer
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
  
# Create your views here.



  
class HelloView(APIView):
    permission_classes = (IsAuthenticated, )
  
    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)

def show(request):
    return render(request,'index.html')

def button(request):
    return render(request,'button.html')

def login(request):
    return render(request,'signin.html')

def typography(request):
    return render(request,'typography.html')

def element(request):
    return render(request,'element.html')

def usersignup(request):
    return render(request,"signup.html")

def Dashboard(request):
    return render(request, 'table.html')

def widget(request):
    return render(request,'widget.html')

def form(request):
    return render(request,'form.html')

def chart(request):
    return render(request,'chart.html')

def error(request):
    return render(request,'404.html')

def blank(request):
    return render(request,'blank.html')

@csrf_exempt
def signup(request):
    print("4444")
    if request.method == 'POST':
        firstName = request.POST.get("firstName")
        lastName = request.POST.get('lastName')
        email = request.POST.get('email')
        mobileNo = request.POST.get('mobileNo')
        Address = request.POST.get('Address')
        password = request.POST.get('password')
        print("333",firstName)
        print("333",password)
        user = User.objects.create_user(
            firstName = firstName,
            lastName = lastName,
            email = email,
            mobileNo = mobileNo,
            Address = Address,
            password = password
            
        )
        print("@@@@@@@@@@@@@@@@@" ,user)
        login(request,user)
        subject = 'Hi this is testing mail'
        message = 'hi {user.firstName}  thanks for registration to our website'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [user.email,]
        send_mail(subject, message, email_from, recipient_list)
        print("fdfdfdfdfdfdf")
        # return redirect('/dashboard')
        return JsonResponse({"message":"mail sent "},safe=False,status=200)
    # return render(request,'signup.html')
    return JsonResponse({"message":"error occured"},safe=False,status=404)




class UserSignupAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Dataa = request.data
            serializer = UserSerializer(data = Dataa)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Regstration Successfully"},safe=False,status=200)
                # return render(request, )
            else:
                return JsonResponse({"message":"Something Goes Wrong"},safe=False,status=404)
        except Exception as e:
            return  JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

class userLoginAPI(APIView):
    def post(self,request, *args, **kwargs):
        email = request.data.get('email',None)
        password = request.data.get('password',None)
        try:
            get_data = User.objects.get(email=email, password=password)
            if get_data:
                # return render(request,'table.html')
                return JsonResponse({"message":"Login succeefully"},safe=False,status=200)
            else:
                # return render(request,'404.html')
                return JsonResponse({"message":"Something goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

class MyProfileAPI(APIView):
    def get(self,request):
        try:
            id = request.GET['id']
            get_data = User.objects.filter(id=id)
            serializer = UserSerializer(get_data, many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"messsage":"Internal server error {}".format(e)},safe=False,status=500)

class MainCategoryAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Data = request.data
            serializer = MainCategorySerializer(data = Data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something Goes Wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def get(self, request):
        try:
            get_data = mainCategory.objects.all()
            serializer = MainCategorySerializer(get_data, many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def delete(self, request):
        try:
            id = request.GET['id']
            get_data = mainCategory.objects.filter(id=id).delete()
            MainCategorySerializer(get_data, many=True)
            return JsonResponse({"message":"Data deleted successfully"}, safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internals erver error {}".format(e)},safe=False,status=500)
    def put(self, request):
        try:
            data = request.data
            id = data['id']
            get_data = mainCategory.objects.filter(id=id)
            serializer = MainCategorySerializer(instance=get_data, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"data updated successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)


class SubCategoryAPI(APIView):
    def post(self, request):
        try:
            Data = request.data
            serializer = SubCategorySerializer(data=Data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something Goes Wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def get(self,request):
        try:
            get_data = SubCategory.objects.all()
            serializers = SubCategorySerializer(get_data,many=True)
            return JsonResponse(serializers.data, safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def delete(self,request):
        try:
            id = request.GET['id']
            get_data = SubCategory.objects.filter(id=id).delete()
            SubCategorySerializer(get_data, many=True)
            return JsonResponse({"message":"Data deleted successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Intenal server error {}".format(e)},safe=False,status=500)
            
            
class ProductAPI(APIView):
    def post(self, request):
        try:
            Data = request.data
            serializers = ProductSerializer(data= Data)
            if serializers.is_valid():
                serializers.save()
                return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something Goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"messgae":"Internal server error {}".format(e)},safe=False,status=500)
    def get(self,request):
        try:
            get_data = Product.objects.all()
            serializer = ProductSerializer(get_data, many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def delete(self, request):
        try:
            id = request.GET['id']
            get_data = Product.objects.filter(id=id).delete()
            ProductSerializer(get_data, many=True)
            return JsonResponse({"message":"Data deleted sucessfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)


class OfferAPI(APIView):
    def post(self,request):
        try:
            Data = request.data
            serializer = OfferSerializer(data = Data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def get(self, request):
        try:
            get_data = Offer.objects.all()
            serializer = OfferSerializer(get_data, many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
    def delete(self,request):
        try:
            id = request.GET['id']
            get_data = Offer.objects.filter(id=id).delete()
            OfferSerializer(get_data, many=True)
            return JsonResponse({"message":"Data deleted successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
        
class DiscountAPI(APIView):
    def post(self, request):
        try:
            Data = request.data
            Serializer = DiscountSerializer(data=Data)
            if Serializer.is_valid():
                Serializer.save()
                return JsonResponse({"message":"Data added successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

    def get(self, request):
        try:
            get_data = Discount.objects.all()
            serializer = DiscountSerializer(get_data,many=True)
            return JsonResponse(serializer.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

    def delete(self, request):
        try:
            id = request.GET['id']
            Discount.objects.filter(id=id).delete()
            return JsonResponse({"message":"data delete successfully"},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)


class AddToCartAPI(APIView): 
    def post(self,request):
        try:
            Data = request.data
            id = Data['id']
            get_data = Product.objects.filter(productId=id)
            serializer = ProductSerializer(get_data, many=True) 
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Data add to cart successfully"},safe=False,status=200)
            else:
                return JsonResponse({"message":"Something goes wrong"},safe=False,status=404)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

class AddToWishlistAPI(APIView):
    def post(self, request):
        try:
            Data = request.data
            productId = Data['productId']
            get_data = Product.objects.filter(id=productId)
            serializers = ProductSerializer(get_data, many=True)
            if serializers.is_valid():
                serializers.save()
                message = {
                    "status":200,
                    "result":"Product added to wishlist"
                 }
                return JsonResponse(message, safe=False,status=200)
            else:
                return JsonResponse({"message":"Product not found"},safe=False,status=404)
        except Exception as e:
            message = {
                "status":404,
                "result":"Internal server error {}".format(e)
            }
            return JsonResponse(message,safe=False,status=500)

class CartListAPI(APIView):
    def get(self, request):
        try:
            get_data = Product.objects.all()
            ProductSerializer(get_data,many=True)
            return JsonResponse(serializers.data,safe=False,status=200)
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
            
            
# class WishlistAPI(APIView):
#     def get(self, request):
#         try:
#             get_data = 

