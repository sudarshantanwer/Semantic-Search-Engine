import os
import streamlit as st
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Load API Key from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# App title
st.title("📚 Semantic Search Chatbot")

# Load and prepare documents
@st.cache_resource
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

# Ask user input
query = st.text_input("Ask a question:")

# Search and display result
if query:
    results_with_scores = vectordb.similarity_search_with_score(query, k=5)
    sorted_results = sorted(results_with_scores, key=lambda x: x[1])
    
    MIN_SCORE = 0.2
    filtered = [res for res, score in sorted_results if score >= MIN_SCORE]

    if filtered:
        st.subheader("Top Match:")
        st.success(filtered[0].page_content)
    else:
        st.warning("Sorry, no relevant answer found.")
