from typing import List, Optional

from fastapi import Depends, FastAPI
from starlette.responses import RedirectResponse
import random
import string
from loguru import logger
import json

from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
from langchain_text_splitters import CharacterTextSplitter

from dotenv import load_dotenv
import os 
load_dotenv()

app = FastAPI()


## load the parsed pages 
with open('./data/pages.json') as f: 
    pages = json.load(f)
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = [
    Document(
        page_content=page_content, 
        metadata={"page_number":page_number})
    for page_number, page_content in 
    zip(pages['page_numbers'],pages['page_content'])
]

texts = text_splitter.split_documents(docs)
logger.info(f"loaded {len(texts)} from file") 

## load the law book into a vector store plitter

embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(texts, embeddings)


@app.get("/")
async def root():
    return RedirectResponse(app.docs_url)


@app.get("/get_response")
@app.get("/get_response/")
async def get_repsonse():
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=30))
    return res