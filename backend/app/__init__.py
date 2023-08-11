import time
from functools import lru_cache

from fastapi.responses import JSONResponse
from parser.subtitle import parse_subtitle_text

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, Form, Request, Response, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from api.security import create_access_token, jwt_token_required
from logger import logger
from tokenizer.tokenizer import get_japanese_pronounciation, tokenize_japanese_text

load_dotenv(".env")


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def index(request: Request):
    return "OK"


@app.get("/api/checkstatus")
@jwt_token_required
def checkstatus(request: Request):
    return {"message": "OK"}


@app.post("/api/v1/jwt")
def jwt_token(request: Request):
    _ = request.json()
    return {
        "message": "success",
        "token": create_access_token(
            data={"sub": "1234567890", "scopes": ["me"]},
        ),
    }


@lru_cache(maxsize=10000)
def make_pronounciation_response(token):
    return {
        "token": token,
        "pronounciation": get_japanese_pronounciation(token),
    }


@app.post("/api/v1/subtitle/process/file")
@jwt_token_required
async def process_file(request: Request, file: UploadFile = File(...)):
    #
    # TODO: Implement server side events
    #
    start = time.time()
    contents = await file.read()

    response = []
    try:
        for subtitle in parse_subtitle_text(contents.decode("utf-8")):
            tokens = tokenize_japanese_text(subtitle.content)
            response.append(
                {
                    "start": subtitle.start.total_seconds(),
                    "end": subtitle.end.total_seconds(),
                    "content": list(map(make_pronounciation_response, tokens)),
                }
            )
    except ValueError:
        return {"error": "Invalid SRT file", "processed_content": []}, 400
    logger.info(f"Processing took {time.time() - start} seconds")
    return {"processed_content": response}


# @app.options("/api/v1/subtitle/process/text")
# async def process_text_options():
#     response_headers = {
#         "Access-Control-Allow-Origin": "*",
#         "Access-Control-Allow-Methods": "POST",
#         "Access-Control-Allow-Headers": "Content-Type, Authorization",
#         "Access-Control-Allow-Credentials": "true",
#     }
#     return JSONResponse(
#         content={},
#         status_code=status.HTTP_200_OK,
#         headers=response_headers,
#     )


@app.post("/api/v1/subtitle/process/text")
@jwt_token_required
async def process_text(request: Request):
    text = (await request.json())["text"]
    tokens = tokenize_japanese_text(text)
    response = list(map(make_pronounciation_response, tokens))
    return {"processed_content": response}
