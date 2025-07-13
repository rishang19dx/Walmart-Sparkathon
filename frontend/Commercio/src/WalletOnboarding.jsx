import React, { useState } from 'react';
import { ethers } from 'ethers';

const BACKEND_URL = "http://localhost:8000";

function WalletOnboarding({ onUserOnboarded, open, onClose }) {
  const [address, setAddress] = useState("");
  const [status, setStatus] = useState("");
  const [user, setUser] = useState(null);

  if (!open) return null;

  const connectWallet = async () => {
    if (!window.ethereum) {
      setStatus("MetaMask not detected. Please install MetaMask.");
      return;
    }
    try {
      const [selectedAddress] = await window.ethereum.request({ method: 'eth_requestAccounts' });
      setAddress(selectedAddress);
      setStatus("Wallet connected. Ready to sign and onboard.");
    } catch (err) {
      setStatus(`Wallet connection failed: ${err.message}. Please try again.`);
    }
  };

  const signAndOnboard = async () => {
    if (!address) return;
    const provider = new ethers.BrowserProvider(window.ethereum);
    const signer = await provider.getSigner();
    const challenge = `Sign this message to login: ${Date.now()}`;
    try {
      setStatus("Signing message...");
      const signature = await signer.signMessage(challenge);
      setStatus("Onboarding...");
      // Send to backend
      const resp = await fetch(`${BACKEND_URL}/users/onboard_wallet`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ address, challenge, signature })
      });
      if (!resp.ok) throw new Error(await resp.text());
      const userObj = await resp.json();
      setUser(userObj);
      setStatus("Onboarding successful!");
      if (onUserOnboarded) onUserOnboarded(userObj);
    } catch (err) {
      setStatus(`Signature or onboarding failed: ${err.message}. Please try again.`);
    }
  };

  return (
    <div className="fixed inset-0 bg-opacity-0 backdrop-blur-xs flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg w-[90%] max-w-md shadow-lg relative">
        <button onClick={onClose} className="absolute top-2 right-2 text-gray-400 hover:text-gray-700 text-2xl">&times;</button>
        <h2 className="text-2xl font-bold mb-4 text-center">Welcome to Commercio</h2>
        <p className="text-gray-600 mb-6 text-center">Connect your wallet to get started with personalized shopping</p>
        {!address ? (
          <button 
            onClick={connectWallet} 
            className="w-full bg-black text-white px-6 py-3 rounded-lg hover:bg-gray-800 transition-colors"
          >
            Connect Wallet
          </button>
        ) : (
          <div className="space-y-4">
            <div className="p-3 bg-gray-100 rounded-lg">
              <div className="text-sm text-gray-600">Connected Address:</div>
              <div className="font-mono text-sm break-all">{address}</div>
            </div>
            <button 
              onClick={signAndOnboard} 
              className="w-full bg-blue-600 text-white px-6 py-3 rounded-lg hover:bg-blue-700 transition-colors"
            >
              Sign & Onboard
            </button>
          </div>
        )}
        {status && (
          <div className="mt-4 p-3 bg-gray-100 rounded-lg text-sm text-gray-700">
            {status}
          </div>
        )}
        {user && (
          <div className="mt-4 p-3 bg-green-100 rounded-lg text-sm text-green-700">
            <div className="font-semibold">Onboarding Successful!</div>
            <div>DID: {user.did}</div>
            <div>User ID: {user.id}</div>
          </div>
        )}
      </div>
    </div>
  );
}

export default WalletOnboarding;