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
embedding = OpenAIEmbeddings(
    model="text-embedding-3-small",
    openai_api_key=OPENAI_API_KEY
)

# Setup Chroma vector store with persistence
vectordb = Chroma.from_documents(docs, embedding, persist_directory="./chroma_db")
vectordb.persist()

# Get user query
query = input("Ask a question: ")

# Search top 5 and rank manually
results_with_scores = vectordb.similarity_search_with_score(query, k=5)

# Sort by ascending score (lower = better)
sorted_results = sorted(results_with_scores, key=lambda x: x[1])
print(sorted_results)

# Filter out weak matches (adjust threshold if needed)
MIN_SCORE = 0.2
filtered = [res for res, score in sorted_results if score >= MIN_SCORE]

if filtered:
    print("\nTop Match:\n")
    print(filtered[0].page_content)
else:
    print("\nSorry, no relevant answer found.")