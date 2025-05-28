// src/components/ChatBox.jsx
import React, { useState } from "react";
import axios from "axios";

const ChatBox = () => {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async (e) => {
    e.preventDefault(); // Prevent form submit reload
    if (!query.trim()) return;

    try {
      setLoading(true);
      const response = await axios.post("http://localhost:8000/query", {
        query: query, // ✅ Send just the query string
      });
      setAnswer(response.data.result); // ✅ Update the answer in state
    } catch (error) {
      console.error("API call error:", error);
      setAnswer("Something went wrong. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>📚 Semantic Search Chatbot</h1>
      <form onSubmit={handleAsk}>
        <input
          type="text"
          placeholder="Ask a question..."
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          style={{
            width: "100%",
            padding: "10px",
            fontSize: "16px",
            marginBottom: "1rem",
          }}
        />
        <button type="submit" disabled={loading}>
          {loading ? "Searching..." : "Ask"}
        </button>
      </form>
      <div style={{ marginTop: "1rem" }}>
        {answer && (
          <div>
            <strong>Answer:</strong>
            <p>{answer}</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default ChatBox;
