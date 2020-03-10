#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from rest_framework.authentication import  BaseAuthentication
from mypro import settings
import jwt
from jwt import exceptions
from rest_framework.exceptions import AuthenticationFailed

class JwtQueryParamsAuthentication(BaseAuthentication):


    def authenticate(self, request):
        token = request.query_params.get('token')
        # 1. 切割
        # 2. 解密第二段/判断过期
        # 3. 验证第三段合法性

        salt = settings.SECRET_KEY
        payload = None
        msg = None
        try:
            payload = jwt.decode(token, salt, True)
        except exceptions.ExpiredSignatureError:
            raise AuthenticationFailed({'code': 2001, 'error': 'token已失效'})
        except exceptions.DecodeError:
            raise AuthenticationFailed({'code': 2002, 'error': 'token认证失败'})
        except exceptions.InvalidTokenError:
            raise AuthenticationFailed({'code': 2003, 'error': '非法的token'})


        #三种操作
        #1.抛出异常，后续不再执行
        #2. return一个元组,（1,2）认证通过，在视图中如果调用request.user就是元组的第一个值,request.auth第二个值
        #3. None

        return (payload,token)