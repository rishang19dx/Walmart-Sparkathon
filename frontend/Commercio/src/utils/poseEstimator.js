import {
  FilesetResolver,
  PoseLandmarker
} from '@mediapipe/tasks-vision';

let poseLandmarker = null;

export async function estimatePose(imageElement) {
  if (!poseLandmarker) {
    const vision = await FilesetResolver.forVisionTasks(
      'https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/wasm'
    );

    poseLandmarker = await PoseLandmarker.createFromOptions(vision, {
      baseOptions: {
        modelAssetPath: `https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision@0.10.3/wasm/pose_landmarker_lite.task`,
        delegate: 'GPU',
      },
      runningMode: 'IMAGE',
      numPoses: 1,
    });

  }

  const result = await poseLandmarker.detect(imageElement);
  const keypoints = result.landmarks?.[0];
  if (!keypoints) return null;

  const dist = (a, b) =>
    Math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2);

  return {
    pixelShoulderDistance: dist(keypoints[11], keypoints[12]),
    pixelHipDistance: dist(keypoints[23], keypoints[24]),
    fullBodyPixelHeight: dist(keypoints[0], keypoints[24]),
  };
}
