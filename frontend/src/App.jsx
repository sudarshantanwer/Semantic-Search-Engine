import React from "react";
import ChatBox from "./components/ChatBox";

export default function App() {
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">📚 Semantic Search Chatbot</h1>
      <ChatBox />
    </div>
  );
}
