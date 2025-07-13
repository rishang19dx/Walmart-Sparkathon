import React from 'react';

function ChatBox({ onClose }) {
  return (
    <div className="fixed right-4 bottom-20 w-80 h-96 bg-white shadow-lg border border-gray-300 rounded-lg p-4 flex flex-col z-50">
      <div className="flex justify-between items-center mb-2">
        <h2 className="font-bold">Chat</h2>
        <button onClick={onClose} className="text-sm text-gray-500">X</button>
      </div>
      <div className="flex-1 border p-2 rounded bg-gray-100 overflow-y-auto">
        <p className="text-sm text-gray-500">This is a placeholder chat box.</p>
      </div>
      <input 
        type="text" 
        placeholder="Type your message..." 
        className="border rounded px-2 py-1 mt-2 w-full" 
      />
    </div>
  );
}

export default ChatBox;
