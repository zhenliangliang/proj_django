#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import jwt
import datetime
from mypro import settings

def create_token(payload,timeout=1):
    # 加盐
    salt = settings.SECRET_KEY

    # 构造header
    headers = {
        'type': 'jwt',
        'alg': 'HS256'
    }

    # 构造payload,里面不能定义密码，否则一旦被解密，就会造成安全隐患
    payload['exp'] = datetime.datetime.utcnow()+datetime.timedelta(minutes=1)

    token = jwt.encode(payload=payload, algorithm='HS256', key=salt, headers=headers).decode('utf-8')
    return  token