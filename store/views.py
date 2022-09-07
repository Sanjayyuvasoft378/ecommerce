from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
# from store.models import Offer, Product, SubCategory, User, mainCategory
from .models import *
# from store.serializers import MainCategorySerializer, OfferSerializer, ProductSerializer, SubCategorySerializer, UserSerializer
from .serializers import *

# Create your views here.

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

class UserSignupAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Dataa = request.data
            serializer = UserSerializer(data = Dataa)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message":"Regstration Successfully"},safe=False,status=200)
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
                return render(request,'table.html')
                # return JsonResponse({"message":"Login succeefully"},safe=False,status=200)
            else:
                return render(request,'404.html')
        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

class MyProfileAPI(APIView):
    def get(self,request):
        try:
            id = request.GET['id']
            print("4444444",id)
            get_data = User.objects.filter(id=id)
            print("...........",get_data)
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