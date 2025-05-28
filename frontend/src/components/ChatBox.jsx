// src/components/ChatBox.jsx
import React, { useState } from "react";
import axios from "axios";

const ChatBox = () => {
  const [query, setQuery] = useState("");
  const [answer, setAnswer] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!query.trim()) return;

    setLoading(true);
    try {
      const res = await axios.post("/search", { query });
      setAnswer(res.data.answer);
    } catch (err) {
      setAnswer("Sorry, something went wrong.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", maxWidth: "600px", margin: "auto" }}>
      <h1>📚 Semantic Search Chatbot</h1>
      <input
        type="text"
        placeholder="Ask a question..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyPress={(e) => e.key === "Enter" && handleAsk()}
        style={{
          width: "100%",
          padding: "10px",
          fontSize: "16px",
          marginBottom: "1rem",
        }}
      />
      <button onClick={handleAsk} disabled={loading}>
        {loading ? "Searching..." : "Ask"}
      </button>
      <div style={{ marginTop: "1rem" }}>
        {answer && <div><strong>Answer:</strong><p>{answer}</p></div>}
      </div>
    </div>
  );
};

export default ChatBox;
