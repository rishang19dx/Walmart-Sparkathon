import React, { useState, useEffect } from 'react';
import Chat from './assets/chat.svg';
import Mic from './assets/mic.svg'; // ✅ Import your mic icon

function FloatingChatbox() {
    const [isOpen, setIsOpen] = useState(false);
    const [showPrompt, setShowPrompt] = useState(true);

    useEffect(() => {
        const timer = setTimeout(() => {
            setShowPrompt(false);
        }, 3000);
        return () => clearTimeout(timer);
    }, []);

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
                            <div className="absolute left-9/10 -bottom-2 transform -translate-x-1/2 w-0 h-0 border-l-6 border-r-6 border-t-6 border-l-transparent border-r-transparent border-t-red-600"></div>
                        </div>
                    )}
                    <div className="bg-white border-2 rounded-full p-3 hover:scale-110 transition-transform duration-300">
                        <span className="text-white font-bold">
                            <img src={Chat} className='h-6' />
                        </span>
                    </div>
                </div>
            </div>

            {isOpen && (
                <div className="fixed bottom-20 right-5 w-80 h-96 bg-white shadow-lg border border-gray-300 rounded-lg p-4 z-50">
                    <div className="font-bold mb-2">Chat with us!</div>
                    <div className="h-72 border border-gray-200 rounded p-2 overflow-y-scroll">Chat Messages...</div>
                    <div className="flex items-center gap-2 mt-2">
                        <input
                            type="text"
                            placeholder="Type a message"
                            className="w-full border border-gray-300 rounded p-2 text-sm"
                        />
                        <button className="p-1 rounded-full bg-gray-100 hover:bg-gray-200 transition cursor-pointer">
                            <img src={Mic} alt="mic" className="h-7" />
                        </button>
                    </div>
                </div>
            )}
        </>
    );
}

export default FloatingChatbox;
