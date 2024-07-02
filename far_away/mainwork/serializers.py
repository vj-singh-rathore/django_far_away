from rest_framework.serializers import ModelSerializer
from .models import ItemBook 
from django.contrib.auth.models import User

class ItemBookSerializer(ModelSerializer):
    class Meta:
        model = ItemBook
        fields = '__all__'
        
        
class UserSignUpSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        
class UserSignInSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username',  'password']