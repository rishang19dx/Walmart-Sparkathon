import React, { useState, useEffect } from 'react';
import Chat from './assets/chat.svg';
import Mic from './assets/mic.svg';

function FloatingChatbox({ user }) {
    const [isOpen, setIsOpen] = useState(false);
    const [showPrompt, setShowPrompt] = useState(true);
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");

    useEffect(() => {
        const timer = setTimeout(() => {
            setShowPrompt(false);
        }, 3000);
        return () => clearTimeout(timer);
    }, []);

    const handleSendMessage = async () => {
        if (!input.trim() || !user) return;
        const userMessage = { sender: "user", text: input };
        setMessages(prev => [...prev, userMessage]);

        try {
            const response = await fetch("http://localhost:8000/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    user_id: user.id,
                    query: input
                })
            });
            const data = await response.json();
            const botMessage = { sender: "bot", text: data.response };
            setMessages(prev => [...prev, botMessage]);
        } catch (error) {
            console.error(error);
            setMessages(prev => [...prev, { sender: "bot", text: "Error talking to server." }]);
        }

        setInput("");
    };

    // Only show chat for onboarded users
    if (!user) return null;

    return (
        <>
            <div
                className="fixed bottom-5 right-10 z-50 cursor-pointer"
                onClick={() => setIsOpen(!isOpen)}
            >
                <div className="relative flex flex-col items-end">
                    {showPrompt && (
                        <div className="relative mb-3 bg-red-600 text-white text-xs rounded px-3 py-1 opacity-100 transition-opacity duration-500">
                            Chat with us!
                            <div className="absolute left-8/10 -bottom-2 transform -translate-x-1/2 w-0 h-0 border-l-6 border-r-6 border-t-6 border-l-transparent border-r-transparent border-t-red-600"></div>
                        </div>
                    )}
                    <div className="bg-white border-2 rounded-full p-3 hover:scale-110 transition-transform duration-300">
                        <img src={Chat} className='h-6' />
                    </div>
                </div>
            </div>

            {isOpen && (
                <div className="fixed bottom-20 right-5 w-80 h-96 bg-white shadow-lg border border-gray-300 rounded-lg p-4 z-50 flex flex-col">
                    <div className="font-bold mb-2">Chat with us!</div>
                    <div className="flex-1 border border-gray-200 rounded p-2 overflow-y-scroll space-y-2 text-sm">
                        {messages.map((msg, index) => (
                            <div
                                key={index}
                                className={`p-2 rounded ${msg.sender === 'user' ? 'bg-blue-100 self-end' : 'bg-gray-100 self-start'}`}
                            >
                                {msg.text}
                            </div>
                        ))}
                    </div>
                    <div className="flex items-center gap-2 mt-2">
                        <input
                            type="text"
                            value={input}
                            onChange={(e) => setInput(e.target.value)}
                            placeholder="Type a message"
                            className="w-full border border-gray-300 rounded p-2 text-sm"
                            onKeyDown={(e) => { if (e.key === 'Enter') handleSendMessage(); }}
                        />
                        <button className="p-2 rounded-full bg-gray-100 hover:bg-gray-200 transition">
                            <img src={Mic} alt="mic" className="h-5 w-5" />
                        </button>
                    </div>
                </div>
            )}
        </>
    );
}

export default FloatingChatbox;
