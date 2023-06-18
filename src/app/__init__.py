from fastapi import FastAPI, Request, Depends, Form, Response, status
from fastapi.security import OAuth2PasswordBearer

import jwt
from datetime import datetime, timedelta
from typing import Optional
from functools import wraps

from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from api.security import jwt_token_required, create_access_token

from dotenv import load_dotenv

load_dotenv(".env")


app = FastAPI()


@app.get("/")
def index(request: Request):
    return "OK"


@app.get("/api/checkstatus")
@jwt_token_required
def checkstatus(request: Request):
    return {"message": "OK"}


@app.get("/api/v1/jwt")
def jwt_token(request: Request):
    return {
        "message": "success",
        "token": create_access_token(
            data={"sub": "1234567890", "scopes": ["me"]},
        ),
    }
