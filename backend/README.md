Great! Here's a `README.md` file to document how to set up and run your **monorepo semantic search chatbot** project using **FastAPI (backend)** and **React (frontend)**:

---

## 📚 Semantic Search Chatbot

A full-stack AI-powered chatbot that performs semantic search using OpenAI embeddings and displays results via a React frontend. The backend uses FastAPI and LangChain with Chroma vector DB.

---

### 🔧 Project Structure

```
semantic-search-chatbot/
│
├── backend/
│   ├── main.py               # FastAPI app
│   ├── data/document.txt     # Source text file
│   ├── chroma_db/            # Vector DB will be persisted here
│   ├── .env                  # Contains OPENAI_API_KEY
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── components/ChatBox.jsx
│   │   └── main.jsx
│   ├── index.html
│   └── package.json
│
├── .gitignore
└── README.md
```

---

### ⚙️ Backend Setup (FastAPI + LangChain)

#### 1. Navigate to backend and create virtual environment

```bash
cd backend
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

#### 2. Install dependencies

```bash
pip install -r requirements.txt
```

**Or manually:**

```bash
pip install fastapi uvicorn python-dotenv langchain chromadb openai
```

#### 3. Add your `.env` file in `backend/`:

```
OPENAI_API_KEY=your_openai_api_key
```

#### 4. Start the backend server

```bash
uvicorn main:app --reload
```

Server runs at: [http://localhost:8000](http://localhost:8000)

---

### 💻 Frontend Setup (React + Axios)

#### 1. Navigate to frontend and install dependencies

```bash
cd ../frontend
npm install
```

#### 2. Start the React dev server

```bash
npm run dev
```

App runs at: [http://localhost:5173](http://localhost:5173)

---

### 🔁 How It Works

* Loads `document.txt` and embeds it using OpenAI’s embedding model.
* User inputs a query in the frontend.
* Backend performs similarity search via LangChain+Chroma and returns the top match.
* React displays the best match on the screen.

---

### 🛑 .gitignore Notes

Ensure the following is in your root `.gitignore`:

```
frontend/node_modules
backend/venv
__pycache__/
```

---

### 📦 Useful Scripts

#### Backend

```bash
# Inside backend/
uvicorn main:app --reload
```

#### Frontend

```bash
# Inside frontend/
npm run dev
```

---

Let me know if you'd like to deploy this project (e.g., on Render, Vercel, or EC2).
