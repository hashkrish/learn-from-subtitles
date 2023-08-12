from sqlite3 import OperationalError
import time
from functools import lru_cache

from sqlalchemy.orm import Session
from parser.subtitle import parse_subtitle_text

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, Form, Request, Response, UploadFile, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from api.security import create_access_token, jwt_token_required
from logger import logger
from tokenizer.tokenizer import get_japanese_pronounciation, tokenize_japanese_text
from db.sqlalchemy import JapaneseEnglish, create_tables, get_db

load_dotenv(".env")


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://learn-from-subtitles.netlify.app",
        "http://127.0.0.1:5173",
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/create-tables")
# def create_tables_endpoint():
#     create_tables()
#     return {"message": "OK"}


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
async def process_text(request: Request):
    text = (await request.json())["text"]
    tokens = tokenize_japanese_text(text)
    response = list(map(make_pronounciation_response, tokens))
    return {"processed_content": response}


@lru_cache(maxsize=10000)
def get_ja_en_word(db, word):
    try:
        items = (
            db.query(JapaneseEnglish)
            .filter(JapaneseEnglish.word == word)
            .limit(10)
            .all()
        )
    except OperationalError as e:
        items = {
            "error": "Database error",
            "message": str(e),
        }
    return items


@app.get("/api/v1/translate/ja/en")
async def get_ja_en(request: Request, word: str, db: Session = Depends(get_db)):
    return get_ja_en_word(db, word)
