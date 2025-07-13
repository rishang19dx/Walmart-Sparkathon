import React, { useState } from 'react';
import PoseAnalyzer from './PoseAnalyzer';

export default function SizeFinderModal({ isOpen, onClose, onSubmit }) {
  const [imageFile, setImageFile] = useState(null);
  const [height, setHeight] = useState('');
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setResult(null);
    const file = e.target.files[0];
    if (file) setImageFile(URL.createObjectURL(file));
  };

  const handleResult = (data) => setResult(data);

  const handleConfirm = () => {
    if (result) {
      onSubmit({
        size: result.size,
        sizeCm: result,
        height,
        image: imageFile,
      });
      onClose();
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-opacity-0 backdrop-blur-xs flex items-center justify-center z-50">
      <div className="bg-white p-6 rounded-lg w-[90%] max-w-md shadow-lg">
        <h2 className="text-xl font-bold mb-4">Find Your Size</h2>

        <label className="text-sm">Upload Image:</label>
        <input type="file" accept="image/*" onChange={handleFileChange} className="w-full p-2 border rounded mb-3" />

        <label className="text-sm">Enter Height (cm):</label>
        <input
          type="number"
          value={height}
          onChange={(e) => setHeight(e.target.value)}
          className="w-full p-2 border rounded mb-3"
        />

        {imageFile && height && (
          <PoseAnalyzer imageSrc={imageFile} heightCm={Number(height)} onResult={handleResult} />
        )}

        {result && (
          <div className="text-sm text-green-600 font-medium mt-3 leading-6">
            Height: {height} cm<br />
            Shoulder: <b>{result.shoulderCm.toFixed(1)}</b> cm<br />
            Waist: <b>{result.hipCm.toFixed(1)}</b> cm<br />
            Recommended Size: <b>{result.size}</b>
          </div>
        )}

        <div className="mt-5 flex justify-end gap-2">
          <button className="px-4 py-2 bg-zinc-300 rounded" onClick={onClose}>Cancel</button>
          <button
            className="px-4 py-2 bg-black text-white rounded disabled:opacity-50 cursor-pointer"
            onClick={handleConfirm}
            disabled={!result}
          >
            Use This Size
          </button>
        </div>
      </div>
    </div>
  );
}
