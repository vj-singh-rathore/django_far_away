from django.shortcuts import render ,redirect
from .models import ItemBook
from .serializers import ItemBookSerializer , UserSignUpSerializer ,UserSignInSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, DestroyAPIView,RetrieveAPIView, UpdateAPIView , GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
import jwt


def signout(request):
    logout(request)
    redirect("mainwork/UserSignInView/")

    
    
class ItemCreateview(CreateAPIView):
    queryset =ItemBook.objects.all()
    serializer_class=ItemBookSerializer

class ItemListview(ListAPIView):
    # queryset =ItemBook.objects.all()
    serializer_class=ItemBookSerializer
    def get_queryset(self):
        userId = self.request.query_params.get('userId',1)
        queryset = ItemBook.objects.filter(userId=userId)
        return queryset
    # def get_queryset(self):
    #     userId = self.request.query_params.get('userId')
    #     queryset = ItemBook.objects.filter(userId=userId)
    #     return queryset


class ItemUpdateview(UpdateAPIView):
    queryset =ItemBook.objects.all()
    serializer_class=ItemBookSerializer


class ItemRetrieveview(RetrieveAPIView):
    queryset =ItemBook.objects.all()
    serializer_class=ItemBookSerializer


class ItemDestroyview(DestroyAPIView):
    queryset =ItemBook.objects.all()
    serializer_class=ItemBookSerializer


class TruncateDataview(GenericAPIView):
    serializer_class=ItemBookSerializer
    def delete(self, request):
        userId = self.request.query_params.get('userId')
        
        # queryset = ItemBook.objects.all().delete()
        queryset = ItemBook.objects.filter(userId= userId).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserSignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer
    def post(self, request):
        # if (request.method == 'POST'):
            print(request.data)
            
            uname= request.data['username']
            mail= request.data['email']
            pwd= request.data['password']
            
            user = User.objects.create_user(username=uname, email=mail , password= pwd)
            # print(user.pk)
            userPk=user.pk
            user.save()
            
            
            return Response(status=status.HTTP_201_CREATED, data={'success':True, 'message':'mje hi mje', 'userPk':userPk})



class UserSignInView(CreateAPIView):
    
    # permission_classes=(permissions.AllowAny,),
    
    # if any x-csrf error --then add permission_classes = [permissions.AllowAny] 
    # also from rest_framework import permissions
    
    serializer_class = UserSignInSerializer
    
    def post(self, request):
        # uname = request.data.get('username', ' ')  either gets username or null
        uname = request.data['username']
        pwd = request.data['password']
        encoded_jwt = jwt.encode({"username": uname,"password": pwd}, "secret", algorithm="HS256")
        print(encoded_jwt)
        decoded_jwt=jwt.decode(encoded_jwt, "secret", algorithms=["HS256"])
        print(decoded_jwt)
        
        user = authenticate(username=uname, password= pwd)
        print(user.pk)
        userPk= user.pk
        if user:
            return Response(status=status.HTTP_201_CREATED, data={'success':True, 'message':'mje hi mje' , 'encode':encoded_jwt , 'decode':decoded_jwt, 'userPk':userPk} )
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED, data={'success':False, 'message':'kya yrrr' , 'encode':encoded_jwt , 'decode':decoded_jwt })
            
            