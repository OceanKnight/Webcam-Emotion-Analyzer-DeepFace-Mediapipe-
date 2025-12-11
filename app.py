from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import cv2
from deepface import DeepFace

app = Flask(__name__)
CORS(app)


def analyze_faces(frame_bgr):
    """
    Runs DeepFace (emotion) + Mediapipe (via detector_backend) on full frame.
    Returns list of faces with emotion, confidence, and bounding box.
    """

    try:
        analysis = DeepFace.analyze(
            img_path=frame_bgr,
            actions=["emotion"],
            enforce_detection=False,
            detector_backend="mediapipe",
            prog_bar=False
        )
    except Exception as e:
        print("DeepFace error:", e)
        return []

    # DeepFace may return one dict or a list of dicts
    if isinstance(analysis, list):
        faces = analysis
    else:
        faces = [analysis]

    result_faces = []

    for face in faces:
        dominant_emotion = face.get("dominant_emotion", "unknown")
        emotion_dict = face.get("emotion", {}) or {}

        confidence = 0.0
        if dominant_emotion in emotion_dict:
            confidence = float(emotion_dict[dominant_emotion]) / 100.0

        region = face.get("region", {}) or {}
        x, y = int(region.get("x", 0)), int(region.get("y", 0))
        w, h = int(region.get("w", 0)), int(region.get("h", 0))

        bbox = {
            "xmin": x,
            "ymin": y,
            "xmax": x + w,
            "ymax": y + h
        }

        result_faces.append({
            "emotion": dominant_emotion,
            "confidence": confidence,
            "bbox": bbox
        })

    return result_faces


@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"}), 200


@app.route("/analyze", methods=["POST"])
def analyze():
    file = request.files.get("frame")
    if not file:
        return jsonify({"error": "No frame uploaded"}), 400

    file_bytes = np.frombuffer(file.read(), np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)

    if frame is None:
        return jsonify({"error": "Could not decode frame"}), 400

    faces = analyze_faces(frame)

    return jsonify({
        "faces": faces,
        "num_faces": len(faces),
        "frame_width": frame.shape[1],
        "frame_height": frame.shape[0]
    })


if __name__ == "__main__":
    print("Backend running at http://127.0.0.1:8000")
    app.run(host="0.0.0.0", port=8000, debug=True)
