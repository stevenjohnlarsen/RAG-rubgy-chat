from typing import List, Optional

from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
import random
import string

app = FastAPI()


@app.get("/")
async def root():
    return RedirectResponse(app.docs_url)


@app.get("/get_response")
@app.get("/get_response/")
async def get_repsonse():
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=30))
    return res