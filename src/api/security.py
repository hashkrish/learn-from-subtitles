from datetime import datetime, timedelta
from functools import wraps
from typing import Optional

from config import Config
from fastapi import Request, Response
import jwt


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
                # if the token is valid return the function with the request
                return func(request, *args, **kwargs)
            except jwt.ExpiredSignatureError:
                # if the token is expired return a 401 error
                return Response("Token expired", status_code=401)
            except jwt.InvalidSignatureError:
                # if the token signature is invalid return a 401 error
                return Response("Invalid token signature", status_code=401)
            except jwt.DecodeError:
                # if the token is invalid return a 401 error
                return Response("Invalid token", status_code=401)
        else:
            # if there is no token return a 401 error
            return Response("No token provided", status_code=401)

    return wrapper
