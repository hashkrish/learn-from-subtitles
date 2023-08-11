from datetime import datetime, timedelta
from functools import wraps
from typing import Optional
import asyncio
import inspect

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, DecodeError
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


async def handle_async(fn, *args, **kwargs):
    return await fn(*args, **kwargs)


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

                if inspect.iscoroutinefunction(func):
                    loop = asyncio.new_event_loop()
                    return loop.run_until_complete(func(request, *args, **kwargs))

                return func(request, *args, **kwargs)

            except ExpiredSignatureError:
                return Response("Token expired", status_code=401)

            except InvalidSignatureError:
                return Response("Invalid token signature", status_code=401)

            except DecodeError:
                return Response("Invalid token", status_code=401)
        else:
            # if there is no token return a 401 error
            return Response("No token provided", status_code=401)

    return wrapper
