import { useEffect, useRef } from 'react';

export default function PoseAnalyzer({ imageSrc, heightCm, onResult }) {
  const poseRef = useRef(null);

  useEffect(() => {
    if (!imageSrc || !heightCm) return;

    const img = new Image();
    img.crossOrigin = 'anonymous';
    img.src = imageSrc;

    img.onload = async () => {
      const canvas = document.createElement('canvas');
      const ctx = canvas.getContext('2d');

      const MAX_WIDTH = 600;
      const scale = img.width > MAX_WIDTH ? MAX_WIDTH / img.width : 1;
      canvas.width = img.width * scale;
      canvas.height = img.height * scale;

      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);

      if (!poseRef.current) {
        poseRef.current = new window.Pose({
          locateFile: (file) => `https://cdn.jsdelivr.net/npm/@mediapipe/pose/${file}`,
        });
        poseRef.current.setOptions({
          modelComplexity: 0,
          smoothLandmarks: true,
          enableSegmentation: false,
          minDetectionConfidence: 0.5,
          minTrackingConfidence: 0.5,
        });

        // ✅ Attach onResults only once
        poseRef.current.onResults((results) => {
          if (!results.poseLandmarks) {
            alert('No pose detected');
            return;
          }

          const lm = results.poseLandmarks;
          const dist = (a, b) => {
            const dx = (a.x - b.x) * canvas.width;
            const dy = (a.y - b.y) * canvas.height;
            return Math.sqrt(dx * dx + dy * dy);
          };

          const shoulderPx = dist(lm[11], lm[12]);
          const hipPx = dist(lm[23], lm[24]);
          const heightPx = dist(lm[0], lm[24]);
          const pxPerCm = heightPx / heightCm;

          const shoulderCm = shoulderPx / pxPerCm;
          const hipCm = hipPx / pxPerCm;

          let size = 'Medium';
          if (shoulderCm < 40 && hipCm < 70) size = 'Small';
          else if (shoulderCm < 45) size = 'Medium';
          else if (shoulderCm < 50) size = 'Large';
          else size = 'X-Large';

          console.log("Pose Result:", { shoulderCm, hipCm, size });
          onResult({ shoulderCm, hipCm, size });
        });
      }

      // ✅ Send the image for processing after everything is ready
      await poseRef.current.send({ image: canvas });
    };

    return () => {
      if (poseRef.current) {
        poseRef.current.close();
        poseRef.current = null;
      }
    };
  }, [imageSrc, heightCm, onResult]);

  return null;
}
