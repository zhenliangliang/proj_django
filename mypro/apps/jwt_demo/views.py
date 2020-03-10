from django.shortcuts import render
from rest_framework.views import  APIView
from rest_framework.response import Response
from . import models
import uuid

from  extra_apps.auth import JwtQueryParamsAuthentication
from utils.jwt_auth import create_token
# Create your views here.
"""基于token的认证"""
class LoginView(APIView):
    """token用户登录"""
    def post(self,request,*args,**kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')

        user_object = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if not user_object:
            return Response({'code':1000,'error':'用户名或密码错误'})

        random_string = str(uuid.uuid4())

        user_object.token = random_string
        #保存token到数据库
        user_object.save()
        token =  create_token({'id':user_object.id,'name':user_object.username})
        return Response({'code':1001,'data':token})

class OrderView(APIView):
    def get(self,request,*args,**kwargs):
        #.query_params获取从url传参
        token = request.query_params.get("token")
        if not token:
            return Response({'code':2000,'error':'登录成功之后才能访问'})

        user_object = models.UserInfo.objects.filter(token=token).first()
        if not user_object:
            return Response({'code':2001,'error':"token无效"})

        return Response("订单列表")



"""基于jwt认证"""

class JwtLoginView(APIView):
    """基于jwt用户登录"""
    #登录不开启认证
    authentication_classes = []
    def post(self,request,*args,**kwargs):
        user = request.data.get('username')
        pwd = request.data.get('password')

        user_object = models.UserInfo.objects.filter(username=user, password=pwd).first()
        if not user_object:
            return Response({'code': 1000, 'error': '用户名或密码错误'})

        token = create_token({'user_id':user_object.id,'username':user_object.username})
        return Response({'code':1001,'data':token})

class JwtOrderView(APIView):
    def get(self,request,*args,**kwargs):
        print(request.user)
        return Response('订单列表')
