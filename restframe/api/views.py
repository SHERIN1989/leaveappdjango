from django.shortcuts import render
from .serializers import UserRegister,UserDataSerializer
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Leave
from .serializers import LeaveSerializer
from rest_framework import permissions,status
from rest_framework.decorators import api_view



# Create your views here.

class register(APIView):
    
    def post(self,request,format=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token,create=Token.objects.get_or_create(user=account)
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
class welcome(APIView):
    permission_classes =(IsAuthenticated,)
    
    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content) 
@api_view(['GET','POST']) 
def api_leave_list_view(request):
    leave = Leave.objects.all()
    if request.method=='GET':
        data={}
        serializer=LeaveSerializer(leave,many=True)
        return Response(serializer.data)

    if request.method=='POST':
        data={}
        serializer=LeaveSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
            "message": "Data saved successfully"
        }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)