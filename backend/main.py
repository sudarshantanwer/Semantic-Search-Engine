from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.docstore.document import Document
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Allow requests from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load and cache vector DB
def load_vector_store():
    with open("data/document.txt", "r") as f:
        raw_text = f.read()

    blocks = raw_text.strip().split("\n\n")
    docs = [Document(page_content=block.strip()) for block in blocks if block.strip()]

    embedding = OpenAIEmbeddings(
        model="text-embedding-3-small",
        openai_api_key=OPENAI_API_KEY
    )

    vectordb = Chroma.from_documents(docs, embedding, persist_directory="./chroma_db")
    vectordb.persist()
    return vectordb

vectordb = load_vector_store()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def read_root():
    return {"message": "🚀 FastAPI server is running!"}

@app.post("/query")
def query_docs(req: QueryRequest):
    results_with_scores = vectordb.similarity_search_with_score(req.query, k=5)
    sorted_results = sorted(results_with_scores, key=lambda x: x[1])

    MIN_SCORE = 0.2
    filtered = [res.page_content for res, score in sorted_results if score >= MIN_SCORE]

    if filtered:
        return {"result": filtered[0]}
    else:
        return {"result": "Sorry, no relevant answer found."}
    
    # server will run at http://127.0.0.1:8000/
