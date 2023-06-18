import time
from functools import lru_cache
from parser.subtitle import parse_subtitle_text

from dotenv import load_dotenv
from fastapi import Depends, FastAPI, File, Form, Request, Response, UploadFile, status
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates

from api.security import create_access_token, jwt_token_required
from logger import logger
from tokenizer.tokenizer import get_japanese_pronounciation, tokenize_japanese_text

load_dotenv(".env")


app = FastAPI()


@app.get("/")
def index(request: Request):
    return "OK"


@app.get("/api/checkstatus")
@jwt_token_required
def checkstatus(request: Request):
    return {"message": "OK"}


@app.post("/api/v1/jwt")
def jwt_token(request: Request):
    data = request.json()
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
async def process_file(file: UploadFile = File(...)):
    #
    # TODO: Implement server side events
    #
    start = time.time()
    contents = await file.read()

    response = []
    for subtitle in parse_subtitle_text(contents.decode("utf-8")):
        tokens = tokenize_japanese_text(subtitle.content)
        response.append(
            {
                "start": subtitle.start.total_seconds(),
                "end": subtitle.end.total_seconds(),
                "content": list(map(make_pronounciation_response, tokens)),
            }
        )
    logger.info(f"Processing took {time.time() - start} seconds")
    return {"processed_content": response}


@app.post("/api/v1/subtitle/process/text")
async def process_text(text: str = Form(...)):
    tokens = tokenize_japanese_text(text)
    response = list(map(make_pronounciation_response, tokens))
    return {"processed_content": response}
