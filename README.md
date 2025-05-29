# 📚 Semantic Search Chatbot

A full-stack AI-powered chatbot that performs semantic search using OpenAI embeddings and displays results via a React frontend. The backend uses FastAPI and LangChain with Chroma vector DB. This app is both development and production-ready, with support for Docker and deployment to cloud platforms like AWS.

---

## 🔧 Project Structure

semantic-search-chatbot/
│
├── backend/
│ ├── main.py # FastAPI app
│ ├── data/document.txt # Source text file
│ ├── chroma_db/ # Vector DB will be persisted here
│ ├── .env # Contains OPENAI_API_KEY
│ └── requirements.txt
│
├── frontend/
│ ├── src/
│ │ ├── components/ChatBox.jsx
│ │ └── main.jsx
│ ├── index.html
│ └── package.json
│
├── docker-compose.yml
├── .gitignore
└── README.md


---

## 🚀 Deployment Options

This app can be run in two ways:

- ✅ Local Dev Setup (with virtualenv + Yarn)
- 🐳 Docker-based Setup (recommended for production)

---

## 🧪 Local Setup (Dev Mode)

### ⚙️ Backend (FastAPI + LangChain)

1. **Navigate to backend and create virtual environment:**

```bash
cd backend
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt

# Add your .env file in backend with these keys/:
OPENAI_API_KEY=your_openai_api_key

# Start the backend server:
uvicorn main:app --reload

# Runs at: http://localhost:8000



## Frontend (React + Yarn)
# Navigate to frontend and install dependencies:
cd ../frontend
yarn install

# Start the React dev server:
yarn dev
# Runs at: http://localhost:5173




# 🐳 Docker Setup (Production-Ready)
# Recommended for AWS EC2 or any cloud server.

# 📋 Prerequisites
# Docker installed: https://docs.docker.com/get-docker/

# .env file added inside backend/ directory:

OPENAI_API_KEY=your_openai_api_key


# ▶️ Run with Docker Compose
docker-compose up --build

# This builds and starts:

# Backend at http://localhost:8000

# Frontend at http://localhost:5173

# 🔁 Restart / Stop Containers
docker-compose restart        # restart all services
docker-compose down           # stop and remove services


# 🔁 How It Works
# The backend loads data/document.txt and creates embeddings using OpenAI API.

# User submits a query via the React-based frontend.

# The backend finds the most semantically similar chunk using LangChain + Chroma.

# The best-matching response is returned and displayed.


# 🔒 .gitignore Best Practices
# Ensure these are ignored:
frontend/node_modules
backend/venv
__pycache__/
.env




✅ Tech Stack
Frontend: React (Vite), Yarn, Axios

Backend: FastAPI, LangChain, ChromaDB, OpenAI

Dev Tools: Docker, Docker Compose

Cloud Ready: Yes (Recommended for AWS/GCP/Azure)

