import os
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load and prepare document blocks
with open("data/document.txt", "r") as f:
    raw_text = f.read()

# Split based on Q&A pairs
blocks = raw_text.strip().split("\n\n")
docs = [Document(page_content=block.strip()) for block in blocks if block.strip()]

# Create embeddings
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Setup Chroma vector store with persistence
vectordb = Chroma.from_documents(docs, embedding, persist_directory="./chroma_db")
vectordb.persist()

# Get user query
query = input("Ask a question: ")

# Perform similarity search with scores
results_with_scores = vectordb.similarity_search_with_score(query, k=2)

# Define a minimum score threshold (the lower, the more similar)
MIN_SCORE = 0.75  # Chroma score is similarity distance (lower = better)

# Filter based on score
relevant_results = [res for res, score in results_with_scores if score < MIN_SCORE]

if relevant_results:
    print("\nTop Match:\n")
    print(relevant_results[0].page_content)
else:
    print("\nSorry, no relevant answer found.")
