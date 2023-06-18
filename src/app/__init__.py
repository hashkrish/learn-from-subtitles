from dotenv import load_dotenv
from fastapi import Depends, FastAPI, Form, Request, Response, status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from api.security import create_access_token, jwt_token_required

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
