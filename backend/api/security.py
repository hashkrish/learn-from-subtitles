from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

import jwt
from fastapi import Request, Response

from config import Config


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=Config.JWT_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, Config.JWT_SECRET, algorithm=Config.JWT_ALGORITHM
    )
    return encoded_jwt


def jwt_token_required(func):
    @wraps(func)
    def wrapper(request: Request, *args, **kwargs):
        # get the token from the request header
        token = request.headers.get("Authorization", None)
        if token:
            try:
                # decode the jwt token
                _ = jwt.decode(
                    token, Config.JWT_SECRET, algorithms=[Config.JWT_ALGORITHM]
                )
                return func(request, *args, **kwargs)

            except jwt.ExpiredSignatureError:
                return Response("Token expired", status_code=401)

            except jwt.InvalidSignatureError:
                return Response("Invalid token signature", status_code=401)

            except jwt.DecodeError:
                return Response("Invalid token", status_code=401)
        else:
            # if there is no token return a 401 error
            return Response("No token provided", status_code=401)

    return wrapper
