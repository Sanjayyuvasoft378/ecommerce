from django.forms import fields  
from django import forms

from store.models import Hotel

class UserImage(forms.ModelForm):  
    class Meta:  
        # To specify the model to be used to create form  
        model = Hotel
        # It includes all the fields of model  
        fields = '__all__'  
        
        