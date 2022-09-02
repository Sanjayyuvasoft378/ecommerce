from csv import excel_tab
from distutils.command.install_egg_info import safe_name
from shutil import ExecError
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from store.models import User

from store.serializers import UserSerializer

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


class UserSignupAPI(APIView):
    def post(self, request, *args, **kwargs):
        try:
            Dataa = request.data
            serializer = UserSerializer(data = Dataa)
            if serializer.is_valid():
                serializer.save()
            return JsonResponse({"message":"Regstration Successfully"},safe=False,status=200)
        except Exception as e:
            return  JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)

class userLoginAPI(APIView):
    def post(self,request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            get_data = User.objects.get(email=email, password=password)
            if get_data:
                return render(request,'table.html')
            else:
                return render(request,'404.html')

        except Exception as e:
            return JsonResponse({"message":"Internal server error {}".format(e)},safe=False,status=500)
            

class MyProfileAPI(APIView):
    def get(self,request,*args, **kwargs):
        try:
            get_data = User.objects.all()
            return JsonResponse({"result":get_data},safe=False,status=200)
        except Exception as e:
            return JsonResponse({"messsage":"Internal server error {}".format(e)},safe=False,status=500)